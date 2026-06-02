from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import bigquery
from google.oauth2 import service_account
import os

app = FastAPI(title="Planning BI API", description="API para dados do BI Performance integrando com BigQuery")

# Configurar CORS para permitir o frontend rodando local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuração BigQuery
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), '..', 'gcp_key.json')

def get_bq_client():
    if os.path.exists(CREDENTIALS_PATH):
        credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)
        return bigquery.Client(credentials=credentials, project=credentials.project_id)
    else:
        # Tenta usar o default do ambiente se o arquivo não existir
        return bigquery.Client()

@app.get("/api/ebitda")
def get_ebitda(ano: int = Query(None), empresa: str = Query(None)):
    """
    Retorna os KPIs de EBITDA traduzindo a lógica do DAX para SQL.
    Tabela Base: bi-performance.BI_QA.VIZ_BALANCETE_AUTO_BI_NEW
    """
    client = get_bq_client()
    
    # Exemplo de Query estruturada para buscar os dados de Receita e EBITDA
    # Esta query é um esboço que precisará ser refinada de acordo com as views exatas (ex: d_mascara_ebitda)
    query = """
        SELECT 
            SUM(CASE WHEN Query = 'Receita Bruta' THEN vlr ELSE 0 END) as receita_bruta,
            SUM(CASE WHEN Query = 'Receita Líquida' THEN vlr ELSE 0 END) as receita_liquida,
            SUM(CASE WHEN grupo_ebitda = 'Sim' THEN vlr ELSE 0 END) as ebitda
        FROM `bi-performance.BI_QA.VIZ_BALANCETE_AUTO_BI_NEW`
        WHERE 1=1
    """
    
    if ano:
        query += f" AND EXTRACT(YEAR FROM data) = {ano}"
    if empresa and empresa != 'Todas':
        query += f" AND Origem_Operacao = '{empresa}'"
        
    try:
        # mock fallback if no access
        # df = client.query(query).to_dataframe()
        # receita_bruta = float(df['receita_bruta'].iloc[0] or 0)
        # ebitda = float(df['ebitda'].iloc[0] or 0)
        
        # Simulação temporária até o BQ rodar com sucesso
        return {
            "kpis": {
                "receitaBruta": {"value": "R$ 14.5M", "trend": "+2.4%", "isPositive": True},
                "receitaLiquida": {"value": "R$ 12.1M", "trend": "+1.8%", "isPositive": True},
                "ebitda": {"value": "R$ 3.8M", "trend": "+4.2%", "isPositive": True},
                "margemEbitda": {"value": "31.4%", "trend": "-0.5p.p", "isPositive": False}
            },
            "chartEvolucao": {
                "labels": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
                "margem": [28, 29, 31, 30, 31, 31.4],
                "ebitda": [2.5, 2.8, 3.2, 3.1, 3.5, 3.8],
                "receita": [8.9, 9.6, 10.3, 10.3, 11.2, 12.1]
            },
            "chartCascata": {
                "labels": ["Receita Líquida", "CPV", "Despesas ADM", "Despesas COM", "EBITDA"],
                "data": [12.1, -5.2, -1.8, -1.3, 3.8]
            }
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/rentabilidade")
def get_rentabilidade(ano: int = Query(None)):
    return {
        "kpis": {
            "lucroBruto": {"value": "R$ 6.9M", "trend": "+3.1%", "isPositive": True},
            "margemBruta": {"value": "57.0%", "trend": "+1.2p.p", "isPositive": True},
            "lucroLiquido": {"value": "R$ 2.4M", "trend": "-1.5%", "isPositive": False},
            "margemLiquida": {"value": "19.8%", "trend": "-0.8p.p", "isPositive": False}
        },
        "chartMargens": {
            "labels": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
            "margemBruta": [55, 56, 57, 56, 56.5, 57],
            "margemLiquida": [18, 19, 20.5, 20, 19.5, 19.8]
        },
        "chartNaoOperacional": {
            "labels": ["Desp. Financeiras", "Impostos", "Outras Desp."],
            "data": [-800000, -450000, -150000]
        }
    }

@app.get("/api/custos")
def get_custos(mes: str = Query(None)):
    return {
        "kpis": {
            "custoTotal": {"value": "R$ 5.2M", "trend": "+4.5%", "isPositive": False},
            "custoMedio": {"value": "R$ 1.250", "trend": "-2.1%", "isPositive": True},
            "percentualReceita": {"value": "42.9%", "trend": "+1.1p.p", "isPositive": False}
        },
        "chartGrupos": {
            "labels": ["Grupo A", "Grupo B", "Grupo C", "Grupo D", "Grupo E"],
            "atual": [1200, 1500, 800, 2100, 950],
            "anterior": [1150, 1550, 750, 1900, 1000]
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
