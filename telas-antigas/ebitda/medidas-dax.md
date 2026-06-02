# Medidas DAX — EBITDA

## Medidas Identificadas

| Nome da Medida | Fórmula DAX | Tabela | Objetivo | Status |
|---|---|---|---|---|
| `[Receita Bruta]` | `SUM(Fato_Vendas[Valor_Bruto])` | Fato_Vendas | Somar o faturamento bruto das vendas | Pendente |
| `[Receita Líquida]` | `SUM(Fato_Lancamentos[Valor_Liquido])` | Fato_Lancamentos | Somar faturamento líquido deduzido de impostos | Pendente |
| `[EBITDA]` | `CALCULATE([Receita Líquida] - [Custos] - [Despesas], Dim_Contas[Grupo_EBITDA] = "Sim")` | Fato_Lancamentos | Calcular o Lucro Operacional (EBITDA) | Pendente |
| `[Margem EBITDA]` | `DIVIDE([EBITDA], [Receita Líquida], 0)` | Fato_Lancamentos | Percentual de EBITDA sobre a Receita Líquida | Pendente |

## Dependências entre Medidas
- A medida `[Margem EBITDA]` depende diretamente das medidas `[EBITDA]` e `[Receita Líquida]`.
- A medida `[EBITDA]` depende de `[Receita Líquida]`, `[Custos]` e `[Despesas]`.

## Medidas Redundantes
- Nenhuma identificada até o momento.

## Medidas Pendentes de Validação
- [ ] Validar se as regras de depreciação e amortização são excluídas do cálculo de `[EBITDA]` diretamente pela tabela `Dim_Contas` ou por alguma regra DAX embutida.

## Observações Técnicas
- As medidas devem ser migradas com atenção a filtros de contexto implícitos.
