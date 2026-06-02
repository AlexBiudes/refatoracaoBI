# Filtros e Segmentadores — Variação dos Custos

## Filtros Existentes

| Filtro | Campo | Tabela | Tipo | Obrigatório | Observações |
|---|---|---|---|---|---|
| Centro de Custo | `CentroCusto[Nome]` | Dim_CentroCusto | Segmentador (Dropdown) | Não | Filtra por área de responsabilidade |
| Tipo de Custo | `Custo[Tipo]` | Dim_Custo_Tipo | Segmentador (Lista) | Não | Filtra Direto vs Indireto |
| Período | `Calendario[Mes-Ano]` | Dim_Calendario | Filtro superior | Sim | Define o mês/ano de análise |

## Segmentadores
- Tipo de Custo utiliza botões de seleção rápida.
- Centro de Custo usa dropdown de busca rápida.

## Interações entre Filtros
- Filtrar por Centro de Custo atualiza a tabela de desvios por conta e o gráfico de barras comparativo.

## Pendências
- [ ] Mapear se a seleção múltipla de centros de custo gera distorções na exibição dos custos fixos rateados.
