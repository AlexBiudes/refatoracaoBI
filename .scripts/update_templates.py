import os
import glob

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

ebitda_replacements = {
    'Fato_Vendas': 'balancetenew',
    'Fato_Lancamentos': 'balancetenew',
    'Dim_Contas': 'd_mascara_ebitda e d_Plano_Depara',
    'Dim_Calendario': 'dCalendario',
    'Calendario[Ano]': 'dCalendario[Ano]',
    'Calendario[Mes_Nome]': 'dCalendario[Mês]',
    'Dim_Empresa': 'd_Plano_Depara (Origem_Operacao)',
    'Empresa[Nome_Empresa]': 'balancetenew[Origem_Operacao]',
    'Dim_CentroCusto': 'N/A',
    'Dim_Estrutura[Nivel]': 'd_mascara_ebitda[nível 1]',
    'Valor_Lancamento': 'balancetenew[vlr]'
}

rentabilidade_replacements = {
    'Fato_Vendas': 'balancetenew',
    'Fato_Lancamentos': 'balancetenew',
    'Dim_Contas': 'd_plano_dre e d_mascara_DRE',
    'Dim_Calendario': 'dCalendario',
    'Calendario[Ano]': 'dCalendario[Ano]',
    'Calendario[Mes_Nome]': 'dCalendario[Mês]',
    'Dim_Empresa': 'd_Plano_Depara',
    'Empresa[Nome_Empresa]': 'balancetenew[Origem_Operacao]',
    'Dim_CentroCusto': 'N/A',
    'Dim_Estrutura[Nivel]': 'd_mascara_DRE[NÍVEL 1]',
    'Valor_Lancamento': 'balancetenew[vlr]'
}

custos_replacements = {
    'Fato_Custos': 'Relatorio_Custos',
    'Fato_Producao': 'Relatorio_Custos',
    'Dim_Produto': 'd_produtos_custos',
    'Dim_Grupo_Produto': 'd_grupo_de_produtos_custos',
    'Dim_CentroCusto': 'N/A',
    'Dim_Calendario': 'dCalendario',
    'Calendario[Ano]': 'dCalendario[Ano]',
    'Calendario[Mes_Nome]': 'dCalendario[Mês]',
    'Valor_Lancamento': 'Relatorio_Custos[custo_total]'
}

base_dir = r'c:\Users\alex.biudes\Desktop\Documentação\MCP\3telas\telas-antigas'

# Update EBITDA
for md_file in glob.glob(os.path.join(base_dir, 'ebitda', '*.md')):
    if 'medidas-dax' not in md_file:
        replace_in_file(md_file, ebitda_replacements)

# Update Rentabilidade
for md_file in glob.glob(os.path.join(base_dir, 'analise-rentabilidade', '*.md')):
    if 'medidas-dax' not in md_file:
        replace_in_file(md_file, rentabilidade_replacements)

# Update Custos
for md_file in glob.glob(os.path.join(base_dir, 'variacao-custos', '*.md')):
    if 'medidas-dax' not in md_file:
        replace_in_file(md_file, custos_replacements)

print("Templates atualizados.")
