# Glossário e Dicionário de Dados

Este documento mapeia os principais termos técnicos, acrônimos e nomes físicos extraídos do modelo de dados do BI, servindo como ponte entre a nomenclatura contábil, o desenvolvimento front-end e o código DAX.

## Dicionário de Nomenclatura (Modelo PBIX)

* **`balancetenew`**: A tabela fato central de lançamentos contábeis. Recebe os dados de transações originadas no BigQuery.
* **`Query`**: Coluna chave na tabela `balancetenew` que mapeia a descrição contábil para as máscaras estruturais (`d_mascara_ebitda` e `d_plano_dre`). 
* **`vlr`**: Coluna que armazena o valor financeiro do lançamento.
* **`chave_primaria`**: Coluna calculada unindo `conta` e `cnpj`, usada para o relacionamento com a dimensão de "De/Para" (`d_Plano_Depara`).
* **`Origem_Operacao`**: Coluna calculada via DAX indicando de onde a transação se originou (ex: sistema X ou Y).
* **`d_mascara_ebitda` / `d_mascara_DRE`**: Tabelas de dimensão conhecidas como "Máscaras". Elas não possuem valores transacionais, apenas definem a estrutura, níveis hierárquicos, sinais e ordem de exibição das linhas nos visuais de DRE e EBITDA.

## Acrônimos de Negócio

* **BL**: Balanço Patrimonial (referenciado nas máscaras de ativo e passivo, ex: `d_mascara_ativo_BL`).
* **CFS**: Cash Flow Statement (Fluxo de Caixa). O modelo possui uma tabela inteira de medidas para isso (`medidas_cfs`).
* **CPV / CSP**: Custo de Produto Vendido / Custo de Serviço Prestado. Categoria chave no DRE e no cálculo da Margem Bruta.
* **DFC**: Demonstração do Fluxo de Caixa (presente na `d_mascara_dfc`).
* **DRE**: Demonstração do Resultado do Exercício. Tela foco de mapeamento junto com o EBITDA.
* **EBITDA**: *Earnings Before Interest, Taxes, Depreciation, and Amortization* (Lucro Antes de Juros, Impostos, Depreciação e Amortização). Principal indicador operacional a ser exibido.
* **MCD**: Abreviação para McDonalds, um grupo específico de lojas ou franquias monitorado no modelo (`d_lojas_mcd`, `medidas_mcd`).
* **ROIC**: *Return on Invested Capital*. Retorno sobre o capital investido (presente em tabelas como `D_ROIC` e `estrutura_roic`).
* **SG&A**: *Selling, General and Administrative Expenses* (Despesas Compras, Gerais e Administrativas). 

## Termos Técnicos do Projeto

* **MCP (Model Context Protocol)**: Tecnologia usada para o agente Antigravity conversar nativamente com ferramentas externas.
* **TMDL (Tabular Model Definition Language)**: Formato de representação textual legível por humanos dos modelos do Analysis Services / Power BI, usado para ler o código DAX e relacionamentos.
* **POC**: *Proof of Concept* (Prova de Conceito). A etapa atual de refatoração destas 3 telas para HTML/JS/CSS puros sem infraestrutura pesada.
