# Estratégia de Integração

Este documento detalha o planejamento estratégico para conectar o novo ambiente HTML aos dados contidos na plataforma do Power BI através de sua API REST pública.

---

## Objetivo da Integração
Automatizar a extração dos metadados estruturais do relatório (visuais, tabelas, relacionamentos) e permitir a execução assíncrona de consultas de dados em tempo de execução para alimentar os dashboards frontend em HTML.

## Autenticação
O fluxo de autenticação adotará o modelo de **Service Principal** (Entidade de Serviço do Azure AD) integrado ao workspace do Power BI. O token OAuth2 de acesso será renovado periodicamente por um servidor intermediário (backend de API) seguro, impedindo o vazamento de chaves para os navegadores dos usuários.

## Leitura de Relatórios
- A extração técnica consultará a definição estrutural das páginas e visuais do relatório de origem para acelerar o processo de mapeamento do frontend.

## Leitura de Datasets
- Integração para mapeamento da estrutura lógica de tabelas físicas, colunas e relacionamentos diretos do modelo semântico.

## Extração de Metadados
- Uso de scripts em Python ou PowerShell para consumo dos endpoints de administração da API REST, gerando registros JSON descritivos de toda a linhagem de dados do Power BI.

## Limitações
- Limites de requisições diárias da API REST do Power BI (Throttling).
- Necessidade de configuração e licenciamento do workspace em capacidade dedicada (Premium ou Embedded) para liberação de determinados endpoints de leitura avançada e execução de queries DAX.

## Cuidados de Segurança
- Aplicação das diretrizes de menor privilégio para o Service Principal (acesso de leitura restrito aos workspaces mapeados).
- Não compartilhamento de IDs de Locatário (Tenant ID), Client IDs ou Secrets nos arquivos Markdown do repositório.
