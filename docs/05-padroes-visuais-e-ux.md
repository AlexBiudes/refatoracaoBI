# Padrões Visuais e UX (Diretrizes de Design)

Este documento estabelece as diretrizes de usabilidade, layout e experiência visual que guiarão a futura refatoração das telas para HTML.

---

## 1. Princípios de Design Executivo

- **Foco em High-Level**: Tomadores de decisão precisam identificar desvios em menos de 5 segundos. O topo da tela deve ser reservado exclusivamente para os indicadores macro (KPIs principais).
- **Densidade de Informação Equilibrada**: Evite colocar dezenas de tabelas e gráficos em uma única página. Priorize a análise em camadas:
  1. *Dashboard* (Informação consolidada)
  2. *Exploração* (Detalhamento por meio de gráficos secundários e filtros)
  3. *Relatório* (Tabelas analíticas detalhadas)
- **Decluttering (Eliminação de Ruído)**: Remover linhas de grade excessivas, bordas marcadas, sombras pesadas e fundos coloridos em demasia que desviam a atenção dos dados.

## 2. Grid e Estrutura de Layout

- **Layout Fixo vs. Responsivo**: A estrutura web deve usar CSS Grid e Flexbox para se adaptar perfeitamente ao tamanho da tela do dispositivo do usuário, mantendo uma proporção de grid padrão.
- **Divisão Típica da Tela**:
  - **Cabeçalho (Header)**: Nome do painel, status de atualização da carga e seletor de navegação rápida.
  - **Barra de Filtros**: Posicionada preferencialmente no topo ou lateral esquerda, de fácil acesso e recolhível (sidebar colapsável) para economizar espaço de tela.
  - **KPIs (Cards)**: Uma fileira horizontal logo abaixo do cabeçalho contendo de 3 a 5 cards de performance macro.
  - **Área de Gráficos**: A parte central da tela para o cruzamento de tendências temporais e rankings.
  - **Área Detalhada (Tabela/Matriz)**: Localizada no quadrante inferior para visualizações tabulares de suporte.

## 3. Paleta de Cores e Contraste

- A nova solução utilizará uma paleta de cores harmoniosa, com preferência para modo escuro premium (Dark Mode) ou modo claro com fundos neutros.
- **Sinalização Semântica**:
  - **Positivo/Sucesso (Verde)**: Usar tons suaves de verde-esmeralda para indicar desvios positivos ou metas batidas.
  - **Neutro/Aviso (Amarelo/Laranja)**: Tons âmbar para desvios em atenção.
  - **Negativo/Crítico (Vermelho)**: Tons pastéis de vermelho para indicar falhas operacionais, despesas estouradas ou metas não atingidas.
- **Taxonomia de Cores de Gráficos**: Usar uma única cor base para a mesma categoria de dados em toda a navegação (ex: se Receita é azul na tela de EBITDA, deve permanecer azul na tela de Rentabilidade).

## 4. Tipografia e Hierarquia Visual

- Utilização de fontes modernas sem serifa de carregamento rápido (ex: Inter ou Roboto).
- **Escala Tipográfica Recomendada**:
  - Valores de KPI: `32px` a `40px` (negrito, alta legibilidade).
  - Títulos de Seção: `18px` a `22px` (seminegrito).
  - Texto de Legenda / Rótulo: `12px` a `14px` (regular, cor de menor contraste).

## 5. Filtros e Interatividade

- **Filtros Globais**: Selecionar um ano/mês no menu do topo deve propagar instantaneamente para todos os gráficos ativos.
- **Tooltips Customizados**: Ao passar o cursor (hover) em um ponto de dados de um gráfico, exibir um card popup formatado com a informação detalhada e a variação em relação ao mês anterior.
- **Drill-Down Visível**: Indicar visualmente quando um gráfico permite o aprofundamento de nível (ex: clicar no ano para abrir os meses).
