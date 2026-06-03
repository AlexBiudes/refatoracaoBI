import main
import time

empresas = main.get_empresas_cache()
print("Total de empresas:", len(empresas))

valid_companies = []

for emp in empresas:
    if emp == 'Todas' or emp == 'null': continue
    
    ebitda = main.get_ebitda(2024, emp)
    custos = main.get_custos(2024, emp)
    
    # Verifica se encontrou dados em ambas as pontas
    if 'error' not in ebitda and 'error' not in custos:
        # Pega a rentabilidade tbm
        rent = main.get_rentabilidade(2024, emp)
        
        # Garante que tenha valores válidos (nao R$ 0,00)
        eb_val = ebitda.get('kpis', {}).get('ebitda', {}).get('value', 'R$ 0,00')
        ct_val = custos.get('kpis', {}).get('custoTotal', {}).get('value', 'R$ 0,00')
        
        if eb_val != 'R$ 0,00' and ct_val != 'R$ 0,00':
            valid_companies.append({
                'empresa': emp,
                'ebitda': eb_val,
                'lucro_liquido': rent.get('kpis', {}).get('lucroLiquido', {}).get('value', '0'),
                'custo_total': ct_val
            })
            if len(valid_companies) >= 5:
                break

print("Empresas válidas:", valid_companies)
