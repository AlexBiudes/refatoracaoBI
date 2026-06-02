# Pontos de Melhoria — Variação dos Custos

## Melhorias Visuais
- Utilizar cores contrastantes e semanticamente claras para diferenciar Realizado (ex: azul escuro ou cinza elegante) e Orçado (ex: tracejado preto ou barra fina complementar).
- Destaque em vermelho nos desvios negativos que superam 5% do planejado.

## Melhorias de Usabilidade
- Adicionar opção de exportação em planilha CSV formatada para a tabela de desvios.
- Permitir ordenação dinâmica em todas as colunas da tabela de desvios de centro de custo.

## Melhorias Técnicas
- Criar agregações no banco de dados para evitar recalcular variações no nível de transações de diário.

## Melhorias nas Medidas
- Otimizar a lógica de cálculo YoY utilizando funções nativas de Time Intelligence (`SAMEPERIODLASTYEAR`).

## Melhorias nos Gráficos
- Utilizar gráficos do tipo Bullet Chart para comparar a meta de custos contra o realizado.

## Priorização

| Melhoria | Tipo | Prioridade | Impacto | Status |
|---|---|---|---|---|
| M01: Bullet Chart de desvios | Gráficos | Média | Alto | Não Iniciado |
| M02: Alertas visuais contábeis | Visual | Alta | Alto | Não Iniciado |
| M03: Otimização Time Intelligence | Técnica | Alta | Médio | Não Iniciado |
