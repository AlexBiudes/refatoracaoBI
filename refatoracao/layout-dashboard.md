# Layout do Dashboard

Proposta inicial de arranjo e estrutura visual dos elementos para as novas telas.

---

## 1. Header (Cabeçalho)
- **Posição**: Topo fixo da tela (`position: fixed; width: 100%; top: 0;`).
- **Conteúdo**:
  - Logo corporativo (esquerda).
  - Título do Painel Ativo (centro).
  - Links de atalho rápido para as telas: EBITDA, Rentabilidade, Custos.
  - Carimbo de data/hora da última carga de dados + botão de ajuda de regras (direita).

## 2. Área de Filtros
- **Posição**: Logo abaixo do header ou barra lateral retrátil (sidebar).
- **Conteúdo**:
  - Seleção de Ano.
  - Seleção de Mês/Período.
  - Filtros organizacionais (Empresa, Filial, Canal de Vendas).
  - Botão de limpar todos os filtros aplicados.

## 3. Cards Principais (KPIs)
- **Posição**: Faixa horizontal centralizada com largura total.
- **Estrutura**: Grid Flexível de 4 ou 5 colunas que se transforma em coluna única em resoluções mobile.

## 4. Área de Gráficos
- **Estrutura**: Grid de 2 colunas para telas Desktop (proporção 60% e 40%).
- **Lado Esquerdo**: Gráficos de tendências históricas (ex: evolução da margem contínua nos últimos 12 meses).
- **Lado Direito**: Gráficos de composição ou rankings de contribuição (ex: principais categorias que geraram variação de custos).

## 5. Área de Detalhamento
- **Posição**: Seção inferior com controle de abas de navegação.
- **Conteúdo**: Tabela contábil ou analítica detalhada com colunas expansíveis (drill-down).

## 6. Rodapé Técnico (Footer)
- **Posição**: Base da página.
- **Conteúdo**: Notas de direitos autorais, versão do dashboard, link para glossário técnico de negócios e documentação de suporte do Antigravity.
