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

Status inicial: estruturação documental.

## Organização do Repositório

A documentação está organizada por áreas:

- `docs/`: visão geral, objetivos, fases, padrões e glossário
- `telas-antigas/`: mapeamento das telas atuais do Power BI
- `refatoracao/`: proposta de modernização e arquitetura da nova solução
- `backend/`: API em Python (FastAPI) para extração de dados do BigQuery
- `antigravity/`: prompts dos agentes responsáveis pelo projeto
- `html-final/`: entrega front-end HTML/JS conectada à API
- `backlog/`: tarefas, riscos, pendências e decisões
