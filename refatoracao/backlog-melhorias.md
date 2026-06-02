# Backlog de Melhorias

Este backlog registra as oportunidades de melhorias levantadas durante o diagnóstico de usabilidade e técnica das telas do Power BI.

---

| ID | Melhoria | Área | Prioridade | Status | Observações |
|---|---|---|---|---|---|
| B01 | Reduzir poluição visual e excesso de linhas de grade | UX/UI | Alta | Pendente | Aplicável às 3 telas |
| B02 | Otimizar tempo de resposta das consultas de medidas DAX complexas | Técnica | Alta | Pendente | Foco no fechamento mensal |
| B03 | Criar cards de KPIs com minigráficos (sparklines) de tendência integrados | UX/UI | Média | Pendente | Exibe histórico rápido |
| B04 | Implementar menu de filtros retrátil lateral (Sidebar Colapsável) | UX/UI | Média | Pendente | Melhora o aproveitamento de tela |
| B05 | Validar consistência de classificação do plano de contas contábeis de OPEX | Negócio | Alta | Pendente | Alinhamento com Controladoria |
| B06 | Substituir os tradicionais dropdowns longos por segmentadores com caixa de busca rápida | Usabilidade | Alta | Pendente | Essencial para Clientes e Contas |
| B07 | Refatorar cálculo repetitivo de limites de trimestre (UltimoDiaTrimestre) em Medidas Base | Técnica (DAX) | Alta | Mapeado | Encontrado em Vendas_Mes_Atual e custo_mes_atual. Ideal transformar em variável global ou medida base. |
| B08 | Remover redundância de COALESCE(..., 0) agrupando em grupo de cálculo | Técnica (DAX) | Média | Mapeado | Identificado em dezenas de medidas de custo e DRE. Calculation Group é indicado. |
| B09 | Simplificar lógica de variação usando DIVIDE e unificando medidas de Setas | Técnica (DAX) | Alta | Mapeado | Códigos de variação MoM e YoY repetidos com a mesma condicional IF e FORMAT. |
