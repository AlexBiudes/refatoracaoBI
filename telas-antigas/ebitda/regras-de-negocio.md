# Regras de Negócio — EBITDA

## Regras Identificadas

| Regra | Descrição | Origem | Impacto | Status |
|---|---|---|---|---|
| R01: Exclusão de D&A | Custos de depreciação e amortização devem ser excluídos da soma de despesas para o EBITDA. | Controladoria | EBITDA e Margem EBITDA | Pendente |
| R02: Alocação Contábil | Apenas contas com tag `EBITDA_Grupo = "Sim"` na d_mascara_ebitda e d_Plano_Depara entram na soma de custos e despesas. | Controladoria | Cálculo de EBITDA | Pendente |
| R03: Variações cambiais | Lançamentos de variação cambial não realizada devem ser ignorados. | Financeiro | EBITDA Realizado | Pendente |

## Regras Pendentes de Confirmação
- [ ] O tratamento de receitas não operacionais (ex: venda de ativos permanentes) deve constar no cálculo do EBITDA?

## Pontos Críticos
- A desmarcação de contas contábeis no plano de contas do ERP pode alterar retrospectivamente o cálculo do EBITDA caso o histórico não esteja travado.

## Responsáveis pela Validação
- Setor de Controladoria / Auditoria Interna.
