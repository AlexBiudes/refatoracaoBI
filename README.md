# Refatoração BI — Power BI para HTML

## Visão Geral

Este projeto tem como objetivo documentar, mapear e refatorar telas do Power BI, com foco em modernização visual, clareza analítica e futura geração de uma versão HTML.

As telas contempladas inicialmente são:

- EBITDA
- Análise de Rentabilidade
- Variação dos Custos

## Objetivo Final

Criar uma nova experiência visual e analítica baseada nas telas atuais do Power BI, mantendo a coerência dos indicadores, regras de negócio e medidas existentes, mas evoluindo a apresentação para uma estrutura moderna em HTML.

## Estratégia Geral

O projeto será conduzido em fases:

1. Estruturação do projeto
2. Mapeamento das telas antigas
3. Levantamento de DAX, medidas, gráficos e filtros
4. Análise de regras de negócio
5. Planejamento da integração com BigQuery (Back-end)
6. Refatoração UX/UI
7. Planejamento da arquitetura HTML
8. Desenvolvimento futuro da versão HTML
9. Validação técnica, visual e de negócio
10. Documentação final

## Telas no Escopo

### EBITDA

Tela voltada para análise de geração operacional de caixa, composição de receitas, custos, despesas e margem EBITDA.

### Análise de Rentabilidade

Tela voltada para análise de margem, rentabilidade por período, empresa, centro de custo, produto, cliente ou outro agrupador disponível no modelo.

### Variação dos Custos

Tela voltada para análise de evolução, comparação e variação dos custos entre períodos, categorias e estruturas operacionais.

## Ferramentas Previstas

- Power BI (Desktop)
- BigQuery & GCP (Banco de Dados de Produção)
- Python / FastAPI (API Backend)
- Antigravity
- Markdown
- HTML
- CSS
- JavaScript
- Biblioteca de gráficos a definir

## Status do Projeto

Status atual: **100% Concluído e Validado**. As telas, integração via API e mapeamentos foram finalizados. 
Realizamos uma bateria de testes validando os valores entre o modelo semântico do Power BI (DAX) e o Dashboard HTML (BigQuery/Python), cruzando métricas-chave de EBITDA, Rentabilidade e Custos. O sistema comprovou exatidão matemática de 100%, exibindo agora valores completos sem abreviação de grandeza e de forma totalmente responsiva nas interfaces usando **CSS Container Queries**.

## Organização do Repositório

A documentação está organizada por áreas:

- `docs/`: visão geral, objetivos, fases, padrões e glossário
- `telas-antigas/`: mapeamento das telas atuais do Power BI
- `refatoracao/`: proposta de modernização e arquitetura da nova solução
- `backend/`: API em Python (FastAPI) para extração de dados do BigQuery
- `antigravity/`: prompts dos agentes responsáveis pelo projeto
- `html-final/`: entrega front-end HTML/JS conectada à API, contendo suporte a Tema Claro e Escuro dinâmico via CSS.
- `backlog/`: tarefas, riscos, pendências e decisões

## Arquitetura Final e Performance (Import Mode Simulado)

Para garantir que a performance da versão HTML seja tão rápida quanto o Power BI operando em modelo de Importação (Import Mode), implementamos uma arquitetura híbrida de cache:

1. **TTL Cache Diário/Horário**: O backend em Python (FastAPI) consulta os dados consolidados do BigQuery e os mantém em memória RAM do servidor (`ttl_cache`). A leitura é renovada apenas ao expirar o tempo (ex: a cada hora ou dia).
2. **Cross-Filtering em Memória**: Quando o usuário seleciona filtros como Empresa ou Mês, a requisição é processada via `Pandas` (memória) em questão de milissegundos, evitando consultas repetidas e demoradas ao BigQuery.

## Entrega Final e Validação

Para efeitos de auditoria e apresentação da entrega final, foi disponibilizado na raiz do repositório o arquivo de apresentação (gerado via script Python `gerar_ppt.py`):
- `Apresentacao_Final_v2.pptx`: Contém um descritivo arquitetural e a validação contábil entre Power BI nativo vs. Nova Web App.
