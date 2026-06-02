# Gráficos e Visuais — Análise de Rentabilidade

## Lista de Visuais

| Visual | Tipo | Indicador | Eixo/Linha | Valores | Observações |
|---|---|---|---|---|---|
| Card 1 | KPI Card | Margem de Contribuição | N/A | `[Margem Contribuicao %]` | Exibe a margem de contribuição média |
| Gráfico 1 | Barras Horizontais | Rentabilidade por Cliente | Eixo Y: `Cliente[Nome]` | Eixo X: `[Margem Contribuicao %]` | Ranking de clientes mais rentáveis |
| Matriz 1 | Tabela Matriz | Detalhe Rentabilidade | Linhas: `Produto[Categoria] > Produto[Subcategoria]` | Colunas / Valores: `[Faturamento Líquido]`, `[Margem Contribuicao %]` | Tabela com drill-down |

## Hierarquia Visual Atual
1. Indicadores chave no topo.
2. Gráfico de dispersão e ranking de clientes no centro.
3. Tabela detalhada de produtos na base.

## Problemas Identificados
- Legendas muito pequenas e difíceis de ler.
- Lentidão ao expandir níveis da tabela matriz.

## Sugestões de Modernização
- Utilizar gráficos de dispersão (Scatter Plot) interativos para cruzar Volume vs Margem.
- Implementar paginação e carregamento sob demanda na tabela de produtos.
