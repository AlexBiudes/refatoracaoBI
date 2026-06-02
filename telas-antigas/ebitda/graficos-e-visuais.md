# Gráficos e Visuais — EBITDA

## Lista de Visuais

| Visual | Tipo | Indicador | Eixo/Linha | Valores | Observações |
|---|---|---|---|---|---|
| Card 1 | KPI Card | EBITDA | N/A | `[EBITDA]` | Exibe o valor do EBITDA do mês atual |
| Card 2 | KPI Card | Margem EBITDA | N/A | `[Margem EBITDA]` | Exibe a margem em % |
| Gráfico 1 | Linhas e Colunas | Receita vs EBITDA | Eixo X: `Calendario[Mes-Ano]` | Eixo Y: `[Receita Líquida]`, `[EBITDA]` | Evolução temporal mensal |
| Cascata 1 | Waterfall | DRE Resumido | Categoria: `Dim_Estrutura[Nivel]` | Valor: `[Valor_Lancamento]` | Da Receita Bruta ao EBITDA |

## Hierarquia Visual Atual
1. Cards de KPI no topo da tela.
2. Evolução temporal à esquerda.
3. Demonstração em cascata (DRE resumido) à direita.

## Problemas Identificados
- Excesso de linhas de grade horizontais e verticais no gráfico de linha.
- Título dos visuais longos e confusos.
- Rótulos de dados sobrepostos em resoluções menores.

## Sugestões de Modernização
- Utilizar cards com minigráficos (sparklines) de tendência incorporados.
- Substituir o gráfico de barras/linhas misto por visualizadores separados de maior clareza.
- Implementar tooltips modernos com detalhamento automático da variação mensal.
