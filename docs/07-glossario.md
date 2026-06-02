# Glossário do Projeto

Este glossário define os termos analíticos, técnicos e contábeis empregados em toda a documentação da Refatoração BI.

---

### EBITDA
*Earnings Before Interest, Taxes, Depreciation, and Amortization* (Lucro Antes de Juros, Impostos, Depreciação e Amortização). É o indicador financeiro que representa a geração de caixa operacional da companhia.

### Receita
Fluxo de entrada de recursos financeiros resultante da venda de produtos, mercadorias ou prestação de serviços da empresa.
- **Receita Bruta**: Faturamento total das vendas antes de quaisquer deduções.
- **Receita Líquida**: Receita bruta deduzida de devoluções, abatimentos, descontos comerciais e impostos sobre vendas (ICMS, PIS, COFINS, ISS, etc.).

### Custo
Gastos financeiros diretamente vinculados à produção de bens ou prestação de serviços comercializados pela companhia. Ex: matéria-prima, embalagem, frete de compras, salário dos operários de fábrica.

### Despesa
Gastos necessários para a manutenção da estrutura administrativa, comercial e corporativa da empresa, mas que não estão diretamente ligados ao processo produtivo. Ex: aluguel do escritório central, salários do time de vendas, contas de telefone/internet administrativa.

### Margem
Relação percentual entre um indicador de lucro e a receita de vendas.
- **Margem EBITDA**: `EBITDA / Receita Líquida`
- **Margem de Contribuição**: `(Receita Líquida - Custos Variáveis) / Receita Líquida`

### Rentabilidade
Percentual de retorno obtido sobre um determinado investimento ou atividade. Em BI, frequentemente refere-se à margem final obtida por filial, produto ou cliente.

### Variação Absoluta
A diferença numérica nominal entre dois valores de períodos ou cenários distintos.
- *Fórmula*: `Valor Atual - Valor Anterior` ou `Valor Realizado - Valor Orçado`

### Variação Percentual
A variação proporcional de um indicador expressa em percentagem.
- *Fórmula*: `(Valor Atual - Valor Anterior) / Valor Anterior * 100`

### DAX
*Data Analysis Expressions*. Linguagem de fórmulas e expressões utilizada para manipular e calcular dados em ferramentas de Business Intelligence da Microsoft (como Power BI, Analysis Services e Power Pivot).

### Medida
Uma fórmula de cálculo dinâmico declarada em DAX dentro do modelo semântico do Power BI, que se adapta dinamicamente aos filtros e segmentadores selecionados pelo usuário em tela.

### Dataset (Modelo Semântico)
Conjunto de tabelas, relacionamentos, colunas calculadas e medidas que servem de fonte de dados para estruturar os visuais de um relatório do Power BI.

### Segmentador (Slicer)
Filtro visual adicionado diretamente à tela do dashboard para permitir ao usuário final selecionar valores discretos (anos, filiais, gerentes) para filtrar os dados exibidos nos demais visuais.

### Visual
Qualquer elemento gráfico adicionado na tela do relatório para exibir informações (gráficos de pizza, tabelas, matrizes, cards de KPI, mapas).

### KPI
*Key Performance Indicator* (Indicador-Chave de Desempenho). Métrica quantificável utilizada para avaliar o sucesso de uma organização na busca por seus objetivos estratégicos e metas operacionais.
