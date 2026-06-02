# Regras de Negócio Gerais

Este repositório centraliza as regras de negócio transversais que influenciam as três telas analíticas do projeto. Regras de negócio específicas de cada indicador devem ser documentadas nos respectivos diretórios em `telas-antigas/`.

---

## 1. Regras Conhecidas

### Regra de Cenário (Realizado vs. Orçado)
- Os dados do cenário **Realizado** (Actual) originam-se do sistema ERP contábil/financeiro consolidado.
- Os dados do cenário **Orçado** (Budget) derivam das planilhas de planejamento orçamentário anual importadas pelo time de Controladoria.
- O desvio orçamentário é calculado como: `Variação = Realizado - Orçado` (para receitas e lucro) ou `Variação = Orçado - Realizado` (para custos e despesas).

### Calendário Fiscal Corporativo
- O ano fiscal inicia-se em **01 de Janeiro** e encerra-se em **31 de Dezembro**.
- Comparações de períodos anteriores (YoY) devem sempre comparar datas idênticas (ex: acumulado de Jan-Mai/2026 contra Jan-Mai/2025).

## 2. Impacto por Área

### Impacto no EBITDA
- O EBITDA é estruturado a partir da Receita Líquida, deduzindo os Custos dos Produtos Vendidos (CPV) e as Despesas Operacionais (OPEX), excluindo explicitamente despesas com Depreciação, Amortização, Provisões de Perdas e Resultado Financeiro/Tributário.
- A classificação de contas contábeis no grupo de EBITDA segue o plano de contas oficial homologado pelo setor de Controladoria.

### Impacto na Rentabilidade
- A Margem de Contribuição considera a dedução dos Custos Variáveis de Produção e Impostos sobre Vendas.
- A alocação de custos fixos por Centro de Custo para cálculo da Rentabilidade Líquida segue o modelo de rateio aprovado pela diretoria financeira.

### Impacto nos Custos
- A análise de Variação dos Custos considera a classificação entre Custos Diretos (matéria-prima, insumos de produção e mão de obra fabril) e Custos Indiretos (manutenção de fábrica, energia, depreciação produtiva).

## 3. Regras Pendentes de Validação

- [ ] Critério de classificação de devolução de vendas: reduz diretamente a Receita Bruta ou entra como dedução de Receita?
- [ ] Regras de rateio de despesas corporativas compartilhadas (ex: TI, RH e Diretoria): os centros de custos produtivos recebem rateio destas áreas na visualização da Rentabilidade ou a Rentabilidade é apresentada apenas a nível de margem direta?
- [ ] Regras de câmbio para relatórios consolidados em moeda estrangeira (se aplicável).

## 4. Responsáveis por Validação Técnica e de Negócio

| Área | Responsável | Papel no Projeto |
|---|---|---|
| Controladoria / Financeiro | A definir | Validador de Regras de Negócio e Cálculos Contábeis |
| Engenharia de Dados / BI | A definir | Fornecedor das tabelas de dados e arquitetura do Dataset |
| UX/UI e Frontend | Alex Biudes | Arquiteto e Desenvolvedor da Refatoração Visual |
