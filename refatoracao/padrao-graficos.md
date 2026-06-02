# Padrão de Gráficos

Este documento especifica os tipos de gráficos autorizados e os padrões visuais recomendados para cada tipo de análise nas telas refatoradas.

---

## Tipos de Gráficos Permitidos

### 1. Gráfico de Linha (Line Chart)
- **Uso**: Exibir tendências contínuas de métricas ao longo do tempo (evolução mensal ou diária).
- **Diretrizes**: Linhas suaves (curvas de Bezier), espessura de `3px`, sem excesso de marcadores em cada ponto (usar marcadores apenas em hover).

### 2. Gráfico de Barras (Bar Chart)
- **Uso**: Comparação de métricas discretas entre categorias nominais (ex: faturamento por filial ou cliente).
- **Diretrizes**: Barras dispostas horizontalmente para facilitar a leitura dos rótulos de texto longos das categorias.

### 3. Gráfico de Colunas (Column Chart)
- **Uso**: Comparação cronológica de períodos discretos (ex: custos consolidados por trimestre).
- **Diretrizes**: Barras verticais, com largura controlada para evitar colagem excessiva entre os blocos.

### 4. Gráfico de Cascata (Waterfall Chart)
- **Uso**: Demonstrar o fluxo de conciliação financeira acumulada (ex: saindo do faturamento bruto, subtraindo deduções, impostos e custos até chegar no EBITDA).
- **Diretrizes**: Cores semânticas claras para blocos de acréscimo (verde) e decréscimo (vermelho).

### 5. Tabela / Matriz (Table / Matrix)
- **Uso**: Apresentar dados numéricos brutos organizados por múltiplos agrupadores.
- **Diretrizes**: Rótulos numéricos alinhados à direita, cabeçalho fixo, suporte a colunas colapsáveis (drill-down estruturado).

## Comparação de Cenários (Realizado vs. Anterior/Orçado)
- Em gráficos temporais, a métrica do ano atual (**Realizado**) deve utilizar linha contínua e destaque de cor principal. A métrica de referência (**Ano Anterior ou Orçamento**) deve utilizar linha tracejada (`dashed`) em tom cinza neutro para evitar confusão visual.
