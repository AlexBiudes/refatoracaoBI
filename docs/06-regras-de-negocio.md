# Regras de Negócio Transversais

Este documento registra as regras de negócio globais identificadas no modelo semântico `apresentacao_clientes_BI_V2.pbix` que afetam cálculos e exibições em múltiplas telas (EBITDA, DRE/Rentabilidade e Custos).

## 1. Inversão de Sinal (EBITDA / DRE)
A tabela dimensão `d_mascara_ebitda` e a tabela `d_plano_dre` determinam a hierarquia visual.
A coluna `sinal` na máscara de EBITDA instrui o cálculo se o valor vindo do balancete deve ser mantido ou invertido (*-1) para exibição de valores negativos em custos/despesas mantendo a legibilidade contábil do relatório.

## 2. Origem das Operações (De-Para)
Na tabela fato `balancetenew`, a coluna `Origem_Operacao` não vem direto do banco (BigQuery). Ela é uma coluna calculada no DAX do modelo, fazendo um relacionamento e substituição de espaços por underline a partir da tabela de classificação:
`Origem_Operacao = SUBSTITUTE(RELATED('d_Plano_Depara'[origem_operacao]), " ", "_")`
Esta regra é fundamental para os filtros de origem.

## 3. Comportamento Bidirecional em Custos
Para a tela de Variação de Custos, o relatório baseia-se na fato `Relatorio_Custos`.
O filtro de contexto não flui apenas de cima para baixo. Existe **crossFilteringBehavior: BothDirections** entre a fato `Relatorio_Custos` e a dimensão `d_produtos_custos`, e novamente entre `d_produtos_custos` e a hierarquia superior `d_grupo_de_produtos_custos`.

## 4. Subtotais e Categorizações da DRE
A tabela `d_plano_dre` organiza os dados em 4 níveis (Nível 1, Nível 2, Categoria, Subtotal), possuindo uma exclusão explícita na camada do Power Query para a linha `"DRE_Desp_NAO_Operacionais_Receita_nao_operacionalTOTAL"`. 
Qualquer componente HTML precisará respeitar a lógica e identação de subtotais baseada na `ordem certa` dessa tabela.

## 5. Temporalidade e Último Mês
Os cálculos mensais, como `total_mes_atual` e `Saldo_Trimestral`, confiam em funções `LASTDATE` / `EOMONTH` sobre a tabela calendário ou no filtro dinâmico de trimestre, garantindo que o DRE/EBITDA não quebrem se um mês específico não tiver transações registradas.

---
*(Documento será expandido após mapeamento completo das medidas DAX).*
