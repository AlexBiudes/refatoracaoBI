# Medidas DAX — Variação dos Custos

## Medidas Identificadas

| Nome da Medida | Fórmula DAX | Tabela | Objetivo | Status |
|---|---|---|---|---|
| `[Custo Realizado]` | `SUM(Fato_Custos[Valor_Realizado])` | Fato_Custos | Total de custos reais incorridos | Pendente |
| `[Custo Orcado]` | `SUM(Fato_Custos[Valor_Orcado])` | Fato_Custos | Total de custos planejados no orçamento | Pendente |
| `[Desvio Custos]` | `[Custo Orcado] - [Custo Realizado]` | Fato_Custos | Valor absoluto da economia ou estouro | Pendente |
| `[Desvio Custos %]` | `DIVIDE([Desvio Custos], [Custo Orcado], 0)` | Fato_Custos | Variação percentual sobre o orçamento | Pendente |

## Dependências entre Medidas
- `[Desvio Custos]` depende de `[Custo Orcado]` e `[Custo Realizado]`.
- `[Desvio Custos %]` depende de `[Desvio Custos]` e `[Custo Orcado]`.

## Medidas Redundantes
- Nenhuma identificada até o momento.

## Medidas Pendentes de Validação
- [ ] Validar se as regras de tratamento de desvios negativos utilizam a mesma convenção de sinais para todas as categorias.

## Observações Técnicas
- Utiliza a tabela fato de custos, com chaves para centro de custos e conta contábil.
