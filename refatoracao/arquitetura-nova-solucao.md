# Arquitetura da Nova Solução

## Visão da Nova Solução
A nova solução consiste em uma aplicação web moderna que desacopla a visualização de dados da plataforma interna do Power BI. Os dashboards serão renderizados nativamente no navegador utilizando HTML5, CSS3 estruturado e JavaScript moderno.

## Separação entre Dados, Lógica e Visual
Para garantir a modularidade e facilidade de manutenção:
- **Camada de Apresentação (Visual)**: Arquivos HTML estruturados semanticamente com estilização baseada em tokens CSS reutilizáveis.
- **Camada de Controle e Lógica (Controller/JavaScript)**: Scripts responsáveis por realizar requisições assíncronas de dados, tratar respostas de APIs e alimentar os componentes gráficos.
- **Camada de Dados (Data Engine)**: API Gateway que expõe os dados agregados extraídos do Power BI ou de repositórios homologados de dados (ex: Data Lake / DW).

## Futura Integração com API
A aplicação frontend fará requisições autenticadas para um endpoint centralizado que intermedia as requisições com a API REST do Power BI, permitindo:
- Consulta a conjuntos de dados utilizando consultas DAX dinâmicas via endpoint.
- Cache inteligente de respostas de relatórios comuns para melhor performance.

## Estrutura de Componentes
A estrutura base do frontend será organizada de forma modular:
- `/components`: Elementos compartilhados (filtros, headers, cards).
- `/charts`: Configuração e inicialização das instâncias de gráficos (Chart.js ou D3.js).
- `/styles`: CSS estruturado em arquivos focados (variáveis, layout, componentes).
- `/js`: Lógica de chamadas, formatações e escuta de eventos.

## Premissas Técnicas
- **Zero Framework Bloat**: Utilização de JavaScript Vanilla e CSS puro para garantir carregamento sub-segundo.
- **Segurança**: Credenciais e tokens de acesso à API nunca devem ficar visíveis no cliente; toda autenticação e bypass de token da API do Power BI deve ocorrer no servidor backend seguro (Server-to-Server).
