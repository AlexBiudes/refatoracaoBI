# Filtros e Segmentadores — EBITDA

## Filtros Existentes

| Filtro | Campo | Tabela | Tipo | Obrigatório | Observações |
|---|---|---|---|---|---|
| Ano | `Calendario[Ano]` | Dim_Calendario | Segmentador (Lista) | Sim | Filtro de ano fiscal |
| Mês | `Calendario[Mes_Nome]` | Dim_Calendario | Segmentador (Lista) | Não | Filtro de seleção múltipla de meses |
| Empresa | `Empresa[Nome_Empresa]` | Dim_Empresa | Segmentador (Dropdown) | Não | Filtro para seleção de subsidiárias |
| Centro de Custo | `CentroCusto[Cod_Nome]` | Dim_CentroCusto | Filtro lateral | Não | Filtro de apoio técnico |

## Segmentadores
- O ano é selecionado através de uma caixa de seleção horizontal.
- A empresa usa um componente de menu suspenso (dropdown).

## Interações entre Filtros
- Todos os filtros filtram bidirecionalmente as tabelas fato e dimensão associadas no modelo de dados.
- A seleção de uma Empresa filtra automaticamente os centros de custos disponíveis associados a ela.

## Pendências
- [ ] Avaliar se os filtros devem ter comportamento "Apenas Seleção Única" para o Ano, de modo a evitar desconfigurações nas medidas YoY.
