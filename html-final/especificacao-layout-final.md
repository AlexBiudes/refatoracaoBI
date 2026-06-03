# Especificação do Layout Final

Guia contendo a padronização e documentação dos elementos visuais definitivos aplicados na entrega do projeto.

---

## Estrutura Final
- O layout utiliza uma estrutura Side-Navigation (`sidebar`) e uma área principal fluida (`main-content`).
- Tema Base: **Premium Glassmorphism** (Dark Mode com painéis translúcidos).

## Paleta de Cores (Design System)
- **Background Principal**: Deep Dark `#0B0E14` com gradientes radiais.
- **Painéis (Glass)**: Fundo `rgba(21, 26, 35, 0.6)` com Blur de `16px`.
- **Cor Primária**: Neon Cyan `#00F0FF`
- **Cor Secundária**: Deep Purple `#7000FF`
- **Tipografia Escura/Clara**: `#F8F9FA` (Principal) e `#A0AABF` (Secundária)
- **Alerta / Crítico**: Neon Pink `#FF3366`

## Tipografia
- Fonte Principal: **Outfit** (Google Fonts).
- Pesos Utilizados: `300` (Subtitles), `400` (Body), `500` (Navigation), `600` (Table Headers/KPI Trends), `700` (Titles, Values).

## Gráficos
- Biblioteca prevista: Chart.js versão 4.x.
- Estilo: O design de glassmorphism requer que os gráficos não tenham fundos opacos. Eixos com cor transparente ou `rgba(255,255,255,0.1)`.

## Interações
- **Hover Transitions**: `0.3s cubic-bezier(0.4, 0, 0.2, 1)`.
- **KPI Cards Hover**: Scale `1.02` e `translateY(-6px)` acompanhado de uma sombra difusa `--shadow-hover`.
- **Insights**: Shift X (`translateX(8px)`) ao passar o mouse.

