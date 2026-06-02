# Pontos de Melhoria — EBITDA

## Melhorias Visuais
- Adotar um layout de cores mais neutro e sóbrio.
- Substituir bordas quadradas pesadas de gráficos por cantos levemente arredondados e sombras suaves (glassmorphism ou neumorphism moderado).
- Adicionar indicadores visuais de tendência (setas verdes/vermelhas) nos cards de KPIs.

## Melhorias de Usabilidade
- Tornar o painel de filtros colapsável para liberação de espaço em tela.
- Melhorar a legibilidade dos valores nos eixos dos gráficos de barras.

## Melhorias Técnicas
- Otimização do tempo de carregamento da query principal da DRE contábil.
- Revisar dependências das medidas DAX para evitar cálculos redundantes.

## Melhorias nas Medidas
- Simplificar as condicionais da medida principal de EBITDA para torná-la mais eficiente no modelo semântico.

## Melhorias nos Gráficos
- Substituir o gráfico de cascata padrão do Power BI (que possui renderização lenta) por uma versão customizada e mais limpa.

## Priorização

| Melhoria | Tipo | Prioridade | Impacto | Status |
|---|---|---|---|---|
| M01: Redesign de layout | Visual | Alta | Alto | Não Iniciado |
| M02: Painel de Filtros colapsável | Usabilidade | Média | Alto | Não Iniciado |
| M03: Otimização de Medidas | Técnica | Alta | Médio | Não Iniciado |
