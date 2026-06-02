# Endpoints Necessários

Relação dos principais endpoints da API REST do Power BI previstos para o desenvolvimento das integrações técnicas.

---

## 1. Workspaces (Grupos)
- **Endpoint**: `GET https://api.powerbi.com/v1.0/myorg/groups`
- **Objetivo**: Listar os workspaces disponíveis e identificar o ID do grupo onde estão publicados os relatórios EBITDA, Rentabilidade e Custos.

## 2. Reports (Relatórios)
- **Endpoint**: `GET https://api.powerbi.com/v1.0/myorg/groups/{groupId}/reports`
- **Objetivo**: Listar relatórios dentro do workspace selecionado e capturar os IDs específicos de cada painel.

## 3. Pages (Páginas)
- **Endpoint**: `GET https://api.powerbi.com/v1.0/myorg/groups/{groupId}/reports/{reportId}/pages`
- **Objetivo**: Mapear as abas de navegação internas existentes nos relatórios de origem.

## 4. Datasets (Conjuntos de Dados)
- **Endpoint**: `GET https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets`
- **Objetivo**: Identificar os IDs dos modelos semânticos que servem de base para os relatórios.

## 5. Refreshes (Atualizações)
- **Endpoint**: `GET https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}/refreshes`
- **Objetivo**: Monitorar o histórico de cargas e obter a data/hora da última atualização de dados bem-sucedida para exibição no cabeçalho.

## 6. Metadata / Execute Queries (Consulta DAX)
- **Endpoint**: `POST https://api.powerbi.com/v1.0/myorg/datasets/{datasetId}/executeQueries`
- **Objetivo**: Executar instruções DAX diretamente contra o modelo semântico do Power BI para obter os valores agregados em tempo real que alimentarão os gráficos em HTML.

## 7. Permissions (Permissões de Acesso)
- **Endpoint**: `GET https://api.powerbi.com/v1.0/myorg/groups/{groupId}/users`
- **Objetivo**: Validar os níveis de permissão dos usuários no workspace.
