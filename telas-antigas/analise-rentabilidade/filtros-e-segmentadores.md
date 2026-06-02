# Filtros e Segmentadores — Análise de Rentabilidade

## Filtros Existentes

| Filtro | Campo | Tabela | Tipo | Obrigatório | Observações |
|---|---|---|---|---|---|
| Canal de Vendas | `Canal[Descricao]` | Dim_Canal | Segmentador (Lista) | Não | Filtra Varejo, Atacado, E-commerce |
| Categoria Produto | `Produto[Categoria]` | Dim_Produto | Segmentador (Dropdown) | Não | Filtra grupos de produtos |
| Período | `Calendario[Mes-Ano]` | dCalendario | Filtro superior | Sim | Seleção de intervalo temporal |

## Segmentadores
- O canal de vendas é selecionado por meio de caixas de seleção na lateral.
- Categoria de produto usa dropdown hierárquico.

## Interações entre Filtros
- O filtro de Categoria de Produto atualiza a matriz detalhada e o gráfico de ranking.

## Pendências
- [ ] Mapear se a seleção de múltiplos canais gera distorções no cálculo do CMV ponderado.
