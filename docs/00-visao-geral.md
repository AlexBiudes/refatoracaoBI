# Visão Geral do Projeto

## Contexto

Este projeto surge da necessidade de refatorar e modernizar a experiência de consumo de relatórios analíticos estratégicos atualmente construídos no Power BI. O objetivo é migrar estes dashboards para uma interface web nativa em HTML, CSS e JavaScript de alto padrão visual, otimizada para a tomada de decisão executiva.

## Telas do Power BI Envolvidas

Nesta primeira etapa, o escopo contempla três telas críticas de negócio:
1. **EBITDA**: Análise de geração operacional de caixa, demonstrativo de receitas, custos, despesas operacionais e margem EBITDA.
2. **Análise de Rentabilidade**: Detalhamento de margens e rentabilidade segmentada por dimensões organizacionais (período, empresa, unidade, produto, cliente).
3. **Variação dos Custos**: Análise comparativa e evolução de custos operacionais e de produção.

## Objetivo de Modernização

A modernização foca nos seguintes pilares:
- **Experiência Visual Premium (UX/UI)**: Interface limpa, aplicação correta de contraste, tipografia refinada e micro-interações fluidas.
- **Performance de Carregamento**: Resposta imediata aos filtros e transições de tela.
- **Acessibilidade e Responsividade**: Visualização otimizada em múltiplos dispositivos (desktops, tablets e smartphones).
- **Redução de Ruído Visual**: Foco em indicadores de alta relevância (KPIs principais) e gráficos limpos.

## Importância do Mapeamento Técnico

Para garantir a acurácia dos dados e a fidelidade aos conceitos de negócio vigentes no Power BI, é fundamental realizar um mapeamento minucioso de:
- Medidas calculadas e fórmulas em DAX.
- Relacionamentos e origens de dados.
- Regras de negócio embutidas.
- Comportamento de filtros e segmentadores de dados.

## Relação entre Power BI, API, Antigravity e HTML

A engrenagem do projeto baseia-se na seguinte cooperação técnica:
1. **Power BI (Origem)**: Contém o modelo semântico de dados e as regras originais.
2. **Power BI API**: Usada para a extração automatizada de metadados, estrutura de tabelas, layouts de visuais e fórmulas DAX.
3. **Antigravity**: A plataforma onde agentes de IA especialistas orquestram, documentam, validam e auxiliam na codificação do projeto.
4. **HTML (Destino)**: O resultado final consolidado em uma aplicação frontend moderna com consumo dinâmico de dados.
