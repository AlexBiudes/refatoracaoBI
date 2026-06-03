import os
import pandas as pd
from datetime import date
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import bigquery
from google.oauth2 import service_account
from typing import Optional
import time
from functools import wraps

def ttl_cache(maxsize: int, ttl: int):
    cache = {}
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key in cache:
                result, timestamp = cache[key]
                if time.time() - timestamp < ttl:
                    return result
            result = func(*args, **kwargs)
            if len(cache) >= maxsize:
                cache.pop(next(iter(cache)))
            cache[key] = (result, time.time())
            return result
        return wrapper
    return decorator

app = FastAPI(title="Planning BI API", description="API para dados do BI Performance integrando com BigQuery")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), '..', 'gcp_key.json')

def get_bq_client():
    if os.path.exists(CREDENTIALS_PATH):
        credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)
        return bigquery.Client(credentials=credentials, project=credentials.project_id)
    else:
        return bigquery.Client()

def format_currency(value):
    if pd.isna(value): return "R$ 0,00"
    if abs(value) >= 1_000_000:
        return f"R$ {value/1_000_000:.1f}M".replace('.', ',')
    elif abs(value) >= 1_000:
        return f"R$ {value/1_000:.1f}K".replace('.', ',')
    return f"R$ {value:.2f}".replace('.', ',')

def format_percentage(value):
    if pd.isna(value): return "0,0%"
    return f"{value * 100:.1f}%".replace('.', ',')

@ttl_cache(maxsize=1, ttl=3600)
def get_anos_cache():
    client = get_bq_client()
    query = """
        SELECT DISTINCT CAST(SUBSTR(data, 1, 4) AS INT64) as ano
        FROM `bi-performance.BI_QA.VIZ_BALANCETE_AUTO_BI_NEW`
        WHERE data IS NOT NULL
        ORDER BY ano DESC
    """
    try:
        df = client.query(query).to_dataframe()
        return df['ano'].tolist()
    except Exception as e:
        print("Error get_anos_cache:", e)
        return []

@ttl_cache(maxsize=1, ttl=3600)
def get_empresas_cache():
    client = get_bq_client()
    query = """
        SELECT DISTINCT empresa
        FROM `bi-performance.BI_QA.VIZ_BALANCETE_AUTO_BI_NEW`
        WHERE empresa IS NOT NULL AND empresa != ''
        ORDER BY empresa
    """
    try:
        df = client.query(query).to_dataframe()
        return df['empresa'].tolist()
    except Exception as e:
        print("Error get_empresas_cache:", e)
        return []

@ttl_cache(maxsize=10, ttl=3600)
def get_balancete_df(target_ano: int, prev_ano: int):
    client = get_bq_client()
    query = f"""
        SELECT 
            CAST(SUBSTR(data, 1, 4) AS INT64) as ano,
            CAST(SUBSTR(data, 6, 2) AS INT64) as mes,
            empresa,
            descricao as query_name,
            SUM(vlr) as total_vlr
        FROM `bi-performance.BI_QA.VIZ_BALANCETE_AUTO_BI_NEW`
        WHERE CAST(SUBSTR(data, 1, 4) AS INT64) IN ({target_ano}, {prev_ano})
        GROUP BY 1, 2, 3, 4
    """
    return client.query(query).to_dataframe()

@ttl_cache(maxsize=10, ttl=3600)
def get_custos_df(target_ano: int, prev_ano: int):
    client = get_bq_client()
    query = f"""
        SELECT 
            EXTRACT(YEAR FROM SAFE.PARSE_DATE('%d/%m/%Y', data)) as ano,
            EXTRACT(MONTH FROM SAFE.PARSE_DATE('%d/%m/%Y', data)) as mes,
            empresa,
            grupo_produto,
            SUM(custo_total) as custo_total,
            SUM(quantidade) as quantidade,
            SUM(valor_unitario_venda * quantidade) as total_venda
        FROM `bi-performance.BI_PROD.Relatorio_Custos`
        WHERE EXTRACT(YEAR FROM SAFE.PARSE_DATE('%d/%m/%Y', data)) IN ({target_ano}, {prev_ano})
        GROUP BY 1, 2, 3, 4
    """
    return client.query(query).to_dataframe()

@app.get("/api/filtros/anos")
def get_anos():
    return get_anos_cache()

@app.get("/api/filtros/empresas")
def get_empresas():
    return get_empresas_cache()

@app.get("/api/ebitda")
def get_ebitda(ano: int = date.today().year, empresa: Optional[str] = None):
    try:
        target_ano = int(ano)
        prev_ano = target_ano - 1
        
        df = get_balancete_df(target_ano, prev_ano).copy()
        
        if df.empty:
            raise ValueError("Nenhum dado encontrado para os anos selecionados.")

        if empresa and empresa != 'Todas' and empresa != 'null':
            df = df[df['empresa'] == empresa]

        if df.empty:
            raise ValueError("Nenhum dado encontrado para a empresa selecionada.")

        df = df.groupby(['ano', 'mes', 'query_name'])['total_vlr'].sum().reset_index()
        
        df_pivot = df.pivot_table(index=['ano', 'mes'], columns='query_name', values='total_vlr', aggfunc='sum').fillna(0)
        
        def get_col(cols):
            return sum([df_pivot[c] for c in cols if c in df_pivot.columns]) if any(c in df_pivot.columns for c in cols) else 0

        receita_liquida_cols = ['receita bruta', 'Deduções da Receita Bruta', 'DRE_Imp_Incidentes_Sobre_Receita']
        cpv_cols = ['Custo dos Produtos Vendidos', 'Custo dos Serviços', 'custo_vendas']
        desp_adm_cols = ['DRE_Desp_Operacionais_Despesas_administrativas', 'DRE_Desp_Operacionais_Despesas_com_Ocupacao', 'DRE_Desp_Operacionais_Despesas_com_depreciacao']
        desp_com_cols = ['DRE_Desp_Operacionais_Despesas_comerciais', 'DRE_Desp_Operacionais_Despesas_contratuais', 'DRE_Desp_Operacionais_Despesas_com_Propaganda_Publicidade', 'DRE_Desp_Operacionais_Despesas_com_Frota_Transportes']
        
        df_pivot['receita_bruta'] = get_col(['receita bruta'])
        df_pivot['receita_liquida'] = get_col(receita_liquida_cols)
        df_pivot['ebitda'] = get_col(['DRE_ebitda'])
        df_pivot['cpv'] = get_col(cpv_cols) * -1
        df_pivot['desp_adm'] = get_col(desp_adm_cols) * -1
        df_pivot['desp_com'] = get_col(desp_com_cols) * -1
        
        df_pivot['margem_ebitda'] = df_pivot.apply(lambda x: x['ebitda'] / x['receita_liquida'] if x['receita_liquida'] != 0 else 0, axis=1)
        
        df_ano = df_pivot.groupby('ano').sum(numeric_only=True).reset_index()
        df_ano.set_index('ano', inplace=True)
        
        if 'receita_liquida' in df_ano.columns:
            df_ano['margem_ebitda'] = df_ano.apply(lambda x: x['ebitda'] / x['receita_liquida'] if x['receita_liquida'] != 0 else 0, axis=1)
            
        last_row = df_ano.loc[target_ano] if target_ano in df_ano.index else pd.Series(dtype=float).reindex(df_pivot.columns, fill_value=0)
        prev_row = df_ano.loc[prev_ano] if prev_ano in df_ano.index else pd.Series(dtype=float).reindex(df_pivot.columns, fill_value=0)

        def calc_trend(curr, prev):
            if prev == 0: return "0%"
            val = ((curr - prev) / abs(prev)) * 100
            return f"{'+' if val > 0 else ''}{val:.1f}%".replace('.', ',')

        def calc_trend_pp(curr, prev):
            val = (curr - prev) * 100
            return f"{'+' if val > 0 else ''}{val:.1f}p.p".replace('.', ',')

        df_target = df_pivot.reset_index()
        df_target = df_target[df_target['ano'] == target_ano]
        labels_chart = [f"{str(m).zfill(2)}/{str(a)[-2:]}" for a, m in zip(df_target['ano'], df_target['mes'])]

        return {
            "kpis": {
                "receitaBruta": {"value": format_currency(last_row.get('receita_bruta', 0)), "trend": calc_trend(last_row.get('receita_bruta', 0), prev_row.get('receita_bruta', 0)), "isPositive": bool(last_row.get('receita_bruta', 0) >= prev_row.get('receita_bruta', 0))},
                "receitaLiquida": {"value": format_currency(last_row.get('receita_liquida', 0)), "trend": calc_trend(last_row.get('receita_liquida', 0), prev_row.get('receita_liquida', 0)), "isPositive": bool(last_row.get('receita_liquida', 0) >= prev_row.get('receita_liquida', 0))},
                "ebitda": {"value": format_currency(last_row.get('ebitda', 0)), "trend": calc_trend(last_row.get('ebitda', 0), prev_row.get('ebitda', 0)), "isPositive": bool(last_row.get('ebitda', 0) >= prev_row.get('ebitda', 0))},
                "margemEbitda": {"value": format_percentage(last_row.get('margem_ebitda', 0)), "trend": calc_trend_pp(last_row.get('margem_ebitda', 0), prev_row.get('margem_ebitda', 0)), "isPositive": bool(last_row.get('margem_ebitda', 0) >= prev_row.get('margem_ebitda', 0))}
            },
            "chartEvolucao": {
                "labels": labels_chart,
                "margem": (df_target['margem_ebitda'] * 100).round(1).tolist() if not df_target.empty else [],
                "ebitda": (df_target['ebitda'] / 1_000_000).round(2).tolist() if not df_target.empty else [],
                "receita": (df_target['receita_liquida'] / 1_000_000).round(2).tolist() if not df_target.empty else []
            },
            "chartCascata": {
                "labels": ["Receita Líquida", "CPV", "Despesas ADM", "Despesas COM", "Outros", "EBITDA"],
                "data": [
                    float(round(last_row.get('receita_liquida', 0) / 1_000_000, 2)),
                    float(round(last_row.get('cpv', 0) / 1_000_000, 2)),
                    float(round(last_row.get('desp_adm', 0) / 1_000_000, 2)),
                    float(round(last_row.get('desp_com', 0) / 1_000_000, 2)),
                    float(round((last_row.get('ebitda', 0) - (last_row.get('receita_liquida', 0) + last_row.get('cpv', 0) + last_row.get('desp_adm', 0) + last_row.get('desp_com', 0))) / 1_000_000, 2)),
                    float(round(last_row.get('ebitda', 0) / 1_000_000, 2))
                ]
            }
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/rentabilidade")
def get_rentabilidade(ano: int = date.today().year, empresa: Optional[str] = None):
    try:
        target_ano = int(ano)
        prev_ano = target_ano - 1
        
        df = get_balancete_df(target_ano, prev_ano).copy()
        
        if df.empty: raise ValueError("Nenhum dado encontrado para os anos selecionados.")

        if empresa and empresa != 'Todas' and empresa != 'null':
            df = df[df['empresa'] == empresa]
            
        if df.empty: raise ValueError("Nenhum dado encontrado para a empresa selecionada.")

        df = df.groupby(['ano', 'mes', 'query_name'])['total_vlr'].sum().reset_index()

        df_pivot = df.pivot_table(index=['ano', 'mes'], columns='query_name', values='total_vlr', aggfunc='sum').fillna(0)
        
        def get_col(cols):
            return sum([df_pivot[c] for c in cols if c in df_pivot.columns]) if any(c in df_pivot.columns for c in cols) else 0

        df_pivot['receita_liquida'] = get_col(['receita bruta', 'Deduções da Receita Bruta', 'DRE_Imp_Incidentes_Sobre_Receita'])
        df_pivot['lucro_bruto'] = get_col(['DRE_Lucro_bruto'])
        df_pivot['lucro_liquido'] = get_col(['DRE_Lucro_ou_Prejuizo_liquido'])
        
        df_pivot['margem_bruta'] = df_pivot.apply(lambda x: x['lucro_bruto'] / x['receita_liquida'] if x['receita_liquida'] != 0 else 0, axis=1)
        df_pivot['margem_liquida'] = df_pivot.apply(lambda x: x['lucro_liquido'] / x['receita_liquida'] if x['receita_liquida'] != 0 else 0, axis=1)
        
        df_ano = df_pivot.groupby('ano').sum(numeric_only=True).reset_index()
        df_ano.set_index('ano', inplace=True)
        if 'receita_liquida' in df_ano.columns:
            df_ano['margem_bruta'] = df_ano.apply(lambda x: x['lucro_bruto'] / x['receita_liquida'] if x['receita_liquida'] != 0 else 0, axis=1)
            df_ano['margem_liquida'] = df_ano.apply(lambda x: x['lucro_liquido'] / x['receita_liquida'] if x['receita_liquida'] != 0 else 0, axis=1)

        last_row = df_ano.loc[target_ano] if target_ano in df_ano.index else pd.Series(dtype=float).reindex(df_pivot.columns, fill_value=0)
        prev_row = df_ano.loc[prev_ano] if prev_ano in df_ano.index else pd.Series(dtype=float).reindex(df_pivot.columns, fill_value=0)

        def calc_trend(curr, prev):
            if prev == 0: return "0%"
            val = ((curr - prev) / abs(prev)) * 100
            return f"{'+' if val > 0 else ''}{val:.1f}%".replace('.', ',')

        def calc_trend_pp(curr, prev):
            val = (curr - prev) * 100
            return f"{'+' if val > 0 else ''}{val:.1f}p.p".replace('.', ',')

        df_target = df_pivot.reset_index()
        df_target = df_target[df_target['ano'] == target_ano]
        labels_chart = [f"{str(m).zfill(2)}/{str(a)[-2:]}" for a, m in zip(df_target['ano'], df_target['mes'])]

        return {
            "kpis": {
                "lucroBruto": {"value": format_currency(last_row.get('lucro_bruto', 0)), "trend": calc_trend(last_row.get('lucro_bruto', 0), prev_row.get('lucro_bruto', 0)), "isPositive": bool(last_row.get('lucro_bruto', 0) >= prev_row.get('lucro_bruto', 0))},
                "margemBruta": {"value": format_percentage(last_row.get('margem_bruta', 0)), "trend": calc_trend_pp(last_row.get('margem_bruta', 0), prev_row.get('margem_bruta', 0)), "isPositive": bool(last_row.get('margem_bruta', 0) >= prev_row.get('margem_bruta', 0))},
                "lucroLiquido": {"value": format_currency(last_row.get('lucro_liquido', 0)), "trend": calc_trend(last_row.get('lucro_liquido', 0), prev_row.get('lucro_liquido', 0)), "isPositive": bool(last_row.get('lucro_liquido', 0) >= prev_row.get('lucro_liquido', 0))},
                "margemLiquida": {"value": format_percentage(last_row.get('margem_liquida', 0)), "trend": calc_trend_pp(last_row.get('margem_liquida', 0), prev_row.get('margem_liquida', 0)), "isPositive": bool(last_row.get('margem_liquida', 0) >= prev_row.get('margem_liquida', 0))}
            },
            "chartMargens": {
                "labels": labels_chart,
                "margemBruta": (df_target['margem_bruta'] * 100).round(1).tolist() if not df_target.empty else [],
                "margemLiquida": (df_target['margem_liquida'] * 100).round(1).tolist() if not df_target.empty else []
            },
            "chartNaoOperacional": {
                "labels": ["Desp. Financeiras", "Impostos", "Outras Desp."],
                "data": [
                    float(round(last_row.get('DRE_Despesa_financeira', 0) * -1 / 1_000_000, 2)),
                    float(round(last_row.get('DRE_Imposto_de_Renda', 0) / 1_000_000, 2)),
                    float(round(last_row.get('DRE_Desp_NAO_Operacionais_Despesas_nao_operacionais', 0) / 1_000_000, 2))
                ]
            }
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/custos")
def get_custos(ano: int = date.today().year, empresa: Optional[str] = None):
    try:
        target_ano = int(ano)
        prev_ano = target_ano - 1
        
        df = get_custos_df(target_ano, prev_ano).copy()
        if df.empty: raise ValueError("Nenhum dado de custos.")

        if empresa and empresa != 'Todas' and empresa != 'null':
            df = df[df['empresa'] == empresa]

        if df.empty: raise ValueError("Nenhum dado encontrado para a empresa selecionada.")

        df_grp = df.groupby(['ano', 'mes'])[['custo_total', 'quantidade', 'total_venda']].sum().reset_index()
        df_ano = df_grp.groupby('ano').sum(numeric_only=True).reset_index()
        df_ano.set_index('ano', inplace=True)
        
        last_row = df_ano.loc[target_ano] if target_ano in df_ano.index else pd.Series(dtype=float).reindex(df_grp.columns, fill_value=0)
        prev_row = df_ano.loc[prev_ano] if prev_ano in df_ano.index else pd.Series(dtype=float).reindex(df_grp.columns, fill_value=0)

        custo_medio = last_row.get('custo_total', 0) / last_row.get('quantidade', 1) if last_row.get('quantidade', 0) != 0 else 0
        custo_medio_prev = prev_row.get('custo_total', 0) / prev_row.get('quantidade', 1) if prev_row.get('quantidade', 0) != 0 else 0
        
        perc_receita = last_row.get('custo_total', 0) / last_row.get('total_venda', 1) if last_row.get('total_venda', 0) != 0 else 0
        perc_receita_prev = prev_row.get('custo_total', 0) / prev_row.get('total_venda', 1) if prev_row.get('total_venda', 0) != 0 else 0

        def calc_trend(curr, prev):
            if prev == 0: return "0%"
            val = ((curr - prev) / abs(prev)) * 100
            return f"{'+' if val > 0 else ''}{val:.1f}%".replace('.', ',')

        def calc_trend_pp(curr, prev):
            val = (curr - prev) * 100
            return f"{'+' if val > 0 else ''}{val:.1f}p.p".replace('.', ',')

        df_last_ano = df[df['ano'] == target_ano]
        df_prev_ano = df[df['ano'] == prev_ano]
        
        grupos_last = df_last_ano.groupby('grupo_produto')['custo_total'].sum().reset_index()
        grupos_prev = df_prev_ano.groupby('grupo_produto')['custo_total'].sum().reset_index() if not df_prev_ano.empty else pd.DataFrame(columns=['grupo_produto', 'custo_total'])
        
        grupos_merge = pd.merge(grupos_last, grupos_prev, on='grupo_produto', how='outer', suffixes=('_atual', '_anterior')).fillna(0)
        grupos_merge = grupos_merge.sort_values('custo_total_atual', ascending=False).head(5)

        return {
            "kpis": {
                "custoTotal": {"value": format_currency(last_row.get('custo_total', 0)), "trend": calc_trend(last_row.get('custo_total', 0), prev_row.get('custo_total', 0)), "isPositive": bool(last_row.get('custo_total', 0) <= prev_row.get('custo_total', 0))},
                "custoMedio": {"value": format_currency(custo_medio), "trend": calc_trend(custo_medio, custo_medio_prev), "isPositive": bool(custo_medio <= custo_medio_prev)},
                "percentualReceita": {"value": format_percentage(perc_receita), "trend": calc_trend_pp(perc_receita, perc_receita_prev), "isPositive": bool(perc_receita <= perc_receita_prev)}
            },
            "chartGrupos": {
                "labels": grupos_merge['grupo_produto'].tolist(),
                "atual": [float(x) for x in grupos_merge['custo_total_atual']],
                "anterior": [float(x) for x in grupos_merge['custo_total_anterior']]
            }
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
