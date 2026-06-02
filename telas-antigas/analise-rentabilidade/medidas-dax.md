# Medidas DAX — Análise de Rentabilidade

## Medidas Identificadas

| Nome da Medida | Fórmula DAX | Tabela | Objetivo | Status |
|---|---|---|---|---|
| `[Faturamento Líquido]` | `SUM(Fato_Faturamento[Valor_Liquido])` | Fato_Faturamento | Soma do faturamento líquido de devoluções | Pendente |
| `[CMV Total]` | `SUM(Fato_Faturamento[Custo_CMV])` | Fato_Faturamento | Soma do custo de mercadoria vendida | Pendente |
| `[Margem Contribuicao]` | `[Faturamento Líquido] - [CMV Total]` | Fato_Faturamento | Valor da Margem de Contribuição | Pendente |
| `[Margem Contribuicao %]` | `DIVIDE([Margem Contribuicao], [Faturamento Líquido], 0)` | Fato_Faturamento | Percentual de Margem de Contribuição | Pendente |

## Dependências entre Medidas
- `[Margem Contribuicao %]` depende de `[Margem Contribuicao]` e `[Faturamento Líquido]`.
- `[Margem Contribuicao]` depende de `[Faturamento Líquido]` e `[CMV Total]`.

## Medidas Redundantes
- Nenhuma identificada até o momento.

## Medidas Pendentes de Validação
- [ ] Confirmar se há fretes de entrega incluídos no CMV ou se são deduzidos separadamente.

## Observações Técnicas
- As fórmulas DAX são baseadas diretamente na tabela de faturamento de vendas.
