# Método de Extração: Power BI MCP

Em vez de usar a API REST do Power BI Service, a arquitetura deste projeto se baseia na extração direta dos metadados do modelo semântico a partir do Power BI Desktop aberto localmente. 

Para isso, usamos a ferramenta **MCP (Model Context Protocol)**, especificamente o servidor `powerbi-modeling-mcp`.

## Como Funciona

1. **Conexão:** O MCP detecta instâncias locais do Power BI Desktop (via `ListLocalInstances`) e conecta-se à porta interna do Analysis Services da instância aberta (ex: `localhost:62052`).
2. **Extração TMDL:** Usamos a operação `ExportToTmdlFolder` da ferramenta `database_operations` para exportar o modelo semântico inteiro para um formato legível por humanos (TMDL).
3. **Leitura Offline:** O agente Antigravity lê a estrutura de tabelas, relacionamentos e as fórmulas DAX diretamente dos arquivos textuais exportados em `.tmdl-export/`.

## Vantagens desta Abordagem

- **Zero configurações de nuvem:** Dispensa configurações complexas de Azure AD, Service Principals ou permissões de tenant do Power BI Service.
- **Leitura total das medidas:** O formato TMDL exporta 100% das fórmulas DAX do modelo, o que nem sempre é fácil de extrair apenas via DMV queries.
- **Acesso ao fluxo real:** O modelo extraído é o exato arquivo `.pbix` que o usuário está manipulando.
