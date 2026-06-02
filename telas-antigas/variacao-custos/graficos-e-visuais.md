# Gráficos e Visuais — Variação dos Custos

## Lista de Visuais

| Visual | Tipo | Indicador | Eixo/Linha | Valores | Observações |
|---|---|---|---|---|---|
| Card 1 | KPI Card | Custo Realizado | N/A | `[Custo Realizado]` | Exibe o custo real do período |
| Card 2 | KPI Card | Desvio de Custos % | N/A | `[Desvio Custos %]` | Exibe a variação percentual |
| Gráfico 1 | Barras Clusterizadas | Custos por Categoria | Eixo X: `Categoria[Nome]` | Valores: `[Custo Realizado]`, `[Custo Orcado]` | Comparação lado a lado de categorias |
| Tabela 1 | Tabela Simples | Variação por Centro Custo | Linhas: `CentroCusto[Nome]` | Valores: `[Desvio Custos]`, `[Desvio Custos %]` | Detalhamento contendo formatação condicional |

## Hierarquia Visual Atual
1. Cards de desempenho consolidados no topo.
2. Gráfico de barras comparando Real vs Orçado no centro.
3. Tabela com desvios detalhados na base.

## Problemas Identificados
- Cores de barras muito parecidas que dificultam a distinção rápida entre Realizado e Orçado.
- Ausência de tooltips detalhados explicando a causa raiz dos desvios.

## Sugestões de Modernização
- Utilizar gráficos de desvio ou gráficos de bala (Bullet Chart) para melhor comparação de metas.
- Aplicar formatação condicional dinâmica e intuitiva baseada em thresholds aceitáveis.
