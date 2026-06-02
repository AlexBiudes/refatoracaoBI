# Pontos de Melhoria — Análise de Rentabilidade

## Melhorias Visuais
- Evitar cores excessivamente fortes nas tabelas. Usar tons alternados de cinza claro.
- Criar cards de KPI com layout de "progresso" (progress bar) indicando a distância até a meta de margem.

## Melhorias de Usabilidade
- Implementar pesquisa direta por nome de cliente no segmentador de clientes.
- Exibir tooltips explicativos ao passar o mouse sobre o termo "Margem de Contribuição".

## Melhorias Técnicas
- Otimizar indexação da tabela Fato de Faturamento no banco de dados para acelerar o drill-down de categorias.

## Melhorias nas Medidas
- Substituir o uso de `IF` aninhados por `SWITCH` nas medidas DAX de classificação de rentabilidade.

## Melhorias nos Gráficos
- Utilizar gráficos de dispersão (bubble chart) para análise de portfólio de produtos.

## Priorização

| Melhoria | Tipo | Prioridade | Impacto | Status |
|---|---|---|---|---|
| M01: Pesquisa rápida de cliente | Usabilidade | Alta | Alto | Não Iniciado |
| M02: Gráfico de dispersão de margem | Gráficos | Média | Médio | Não Iniciado |
| M03: Otimização de queries | Técnica | Alta | Alto | Não Iniciado |
