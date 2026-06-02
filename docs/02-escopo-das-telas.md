# Escopo das Telas

Este documento define os limites, objetivos e especificações das três telas que compõem o escopo inicial de refatoração do projeto.

---

## 1. EBITDA

### Finalidade
Análise de geração de caixa operacional da companhia. Permite aos executivos compreenderem a composição de receitas, deduções, custos diretos e despesas gerais e administrativas que impactam o resultado operacional (EBITDA) e sua respectiva margem.

### Indicadores Esperados
- **EBITDA (Absoluto)**: R$ gerado na operação.
- **Margem EBITDA**: EBITDA dividido pela Receita Líquida.
- **Receita Bruta / Receita Líquida**: Faturamento e receita após impostos/deduções.
- **Custos Operacionais**: Custos de produtos vendidos ou serviços prestados (CPV/CSP).
- **Despesas Operacionais (OPEX)**: Despesas comerciais, administrativas e gerais.

### Visuais Prováveis
- Cards de KPIs para indicadores macro (EBITDA, Receita Líquida, Custos, Margem).
- Gráfico de cascata (Waterfall) demonstrando a conciliação da Receita Bruta até o EBITDA.
- Gráfico de linha temporal para a evolução mensal da Margem EBITDA x EBITDA Real x EBITDA Orçado.

### Filtros Esperados
- Período (Ano, Mês).
- Unidade de Negócio / Empresa.
- Cenário (Realizado vs. Orçado).

### Perguntas de Negócio Respondidas
- Qual foi o EBITDA operacional do mês atual e o acumulado do ano?
- Atingimos a meta de margem EBITDA definida no orçamento corporativo?
- Quais linhas de despesas operacionais apresentaram maior desvio em relação ao planejado?

---

## 2. Análise de Rentabilidade

### Finalidade
Avaliar a eficiência da geração de lucro em diferentes dimensões de negócio, permitindo identificar quais produtos, clientes, filiais ou canais geram maior retorno financeiro absoluto e percentual.

### Indicadores Esperados
- **Faturamento Líquido**: Receita após devoluções e impostos diretos.
- **Margem de Contribuição**: Receita líquida menos custos e despesas variáveis.
- **Percentual de Margem de Contribuição**: Margem de contribuição dividida pela receita líquida.
- **Lucro Líquido Operacional**: Resultado após custos e despesas fixas atribuídas.

### Visuais Prováveis
- Cards de KPI de rentabilidade macro.
- Gráfico de barras horizontais (ranking) de rentabilidade por Categoria de Produto / Cliente.
- Matriz de detalhamento com expansão (drill-down) contendo a árvore de rentabilidade por canal e filial.
- Gráfico de dispersão (bolhas) cruzando Faturamento vs. Margem de Contribuição por grupo de clientes.

### Filtros Esperados
- Período.
- Canal de Vendas.
- Linha de Produto / Categoria.
- Carteira de Clientes / Vendedor.

### Perguntas de Negócio Respondidas
- Quais filiais operam abaixo do patamar mínimo de rentabilidade aceitável?
- Qual a margem de contribuição média do nosso produto principal?
- O crescimento de faturamento de determinado cliente gerou um aumento proporcional de rentabilidade?

---

## 3. Variação dos Custos

### Finalidade
Identificar flutuações, anomalias e tendências na estrutura de custos (produção, serviços, logística e pessoal), comparando o período atual com períodos anteriores e metas orçadas.

### Indicadores Esperados
- **Custo Total**: Soma de todos os custos mapeados.
- **Desvio Real vs. Orçado (Variação Absoluta e %)**: Diferença em relação ao orçamento.
- **Variação MoM (Mês contra Mês)** e **YoY (Ano contra Ano)**.
- **Custo por Unidade Produzida / Prestada**: Custo médio unitário.

### Visuais Prováveis
- Cards de KPIs com o custo consolidado e indicador visual de aumento/queda de gastos.
- Gráfico de linhas comparando o custo histórico deste ano contra o ano passado.
- Gráfico de barras empilhadas para decomposição do custo por categoria (Insumos, Mão de Obra, Logística, Outros).
- Tabela de desvios com formatação condicional (alertas vermelhos para desvios acima do limite tolerado).

### Filtros Esperados
- Período.
- Centro de Custo.
- Conta Contábil / Categoria de Custo.
- Planta / Unidade Industrial.

### Perguntas de Negócio Respondidas
- Por que o custo de produção subiu no último trimestre?
- Qual categoria de custo apresentou a maior variação nominal em relação ao orçamento?
- O custo unitário médio está estável ou em trajetória de alta?

---

## Pontos Gerais a Mapear em Cada Tela
- Nome exato e tabela de origem de todas as colunas de dados.
- Lógica de filtros laterais e filtros aplicados no nível do visual.
- Ordenações e limites de dados em tabelas e gráficos.
- Regras de formatação condicional vigentes.
