# Estrutura de Componentes

Detalhamento da estrutura planejada de pastas e componentes para o código final.

---

## Estrutura de Diretórios
```text
html-final/
│
├── index.html                  # Página principal orquestradora
├── favicon.ico                 # Favicon corporativo
│
├── css/
│   ├── variables.css           # Tokens de design (cores, espaçamento, fontes)
│   ├── layout.css              # Estrutura de grid principal (Header, Sidebar, Body)
│   ├── components.css          # Estilização de cards, tabelas e botões
│   └── responsive.css          # Regras de media queries
│
├── js/
│   ├── app.js                  # Inicializador geral da aplicação web
│   ├── api.js                  # Gerenciador de requisições AJAX/Fetch
│   ├── components/
│   │   ├── filters.js          # Comportamento de filtros e dropdowns
│   │   └── sidebar.js          # Controle de colapso do menu
│   └── charts/
│       ├── ebitdaChart.js      # Gráficos da tela EBITDA
│       ├── rentabilidadeChart.js # Gráficos da Rentabilidade
│       └── custosChart.js      # Gráficos de Custos
│
└── assets/
    ├── img/                    # Imagens estáticas e logos
    └── fonts/                  # Fontes locais (se aplicável)
```
