# Componentes HTML

Este documento cataloga a especificação estrutural para a futura implementação em HTML/CSS dos blocos de interface do usuário (UI).

---

## Cards de KPI
```html
<!-- Exemplo estrutural de Card de KPI -->
<div class="kpi-card" id="kpi-ebitda">
  <span class="kpi-title">EBITDA Realizado</span>
  <div class="kpi-value-container">
    <span class="kpi-value">R$ 4.2M</span>
    <span class="kpi-badge kpi-badge-positive">+12.4% MoM</span>
  </div>
  <span class="kpi-subtext">vs. R$ 3.8M planejado</span>
</div>
```

## Filtros
- Componentes dropdown interativos e multisseleção baseados em elementos `<select>` nativos customizados ou listas dinâmicas baseadas em tags `<ul>` e `<input type="checkbox">`.

## Containers
- Elementos `<section>` e `<div>` organizados via CSS Grid (`display: grid;`) com espaçamento padronizado de `16px` ou `24px` (`gap`).

## Tabelas
- Tabelas baseadas em tags `<table>`, com cabeçalho fixo (`position: sticky; top: 0;`), formatação condicional de células (`class="val-positive"` ou `class="val-critical"`) e linhas zebra para melhorar a legibilidade.

## Gráficos
- Tags `<canvas>` ou `<svg>` com IDs específicos e únicos (ex: `<canvas id="chart-ebitda-evolucao"></canvas>`) dimensionadas dinamicamente pelas bibliotecas de gráficos JavaScript.

## Cabeçalhos e Menus
- Tags `<header>` e `<nav>` com links de âncoras ou rotas lógicas contendo classes para indicar o estado atual de seleção (`class="nav-link active"`).

## Estados de Loading
- Shimmer effects (efeitos de carregamento com gradientes cinza animados) implementados em CSS para simular a presença dos gráficos e tabelas enquanto os dados da API estão sendo consultados assincronamente.

## Mensagens de Erro
- Card estilizado contendo ícone de aviso técnico e botão de "Repetir tentativa" caso a consulta ou chamada da API falhe por timeout ou problema de permissão.
