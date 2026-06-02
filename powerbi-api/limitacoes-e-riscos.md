# Limitações e Riscos da API

Análise preventiva dos fatores de risco técnicos e de governança na integração com a API REST do Power BI.

---

## 1. Limitações da API REST

- **Throttling (Limite de Requisições)**: O Power BI Service impõe restrições de chamadas consecutivas à API para evitar sobrecarga dos servidores compartilhados.
- **Limite de Execução de Query**: O endpoint de execução de queries DAX (`executeQueries`) possui limite máximo de linhas retornadas por chamada (normalmente 100.000 linhas) e timeout de execução de 2 minutos por query.
- **Licenciamento Pro/Premium**: A execução direta de queries via API exige que o dataset esteja hospedado em um Workspace de capacidade Premium (PPU, capacidades P ou F - Fabric/Embedded). Em workspaces Pro padrão, esse recurso não está totalmente habilitado ou é restrito.

## 2. Riscos de Acesso e Permissões

- **Falta de Permissão de TI**: O administrador de locatário (Tenant Admin) da Microsoft do cliente pode bloquear o uso de Service Principal ou restringir a leitura de metadados de datasets, inviabilizando integrações automatizadas.
- **Segurança da Chave (Secret Expiry)**: O Client Secret gerado no Azure AD expira ciclicamente e a falta de monitoramento pode paralisar as cargas de dados repentinamente.

## 3. Risco de Qualidade de Dados e Interpretação

- **Divergência de Dados**: O tempo de cache da aplicação intermediadora pode gerar divergência de centavos entre o painel oficial do Power BI (atualizado em tempo real ou sob demanda) e o dashboard em HTML.
- **Medidas Não Extraídas**: Fórmulas complexas baseadas em RLS (Row-Level Security) dinâmico podem retornar valores vazios ou incorretos via API se a identidade do usuário final não for passada corretamente nas requisições seguras.
- **Risco de Alterações Silenciosas**: Mudanças de nome de colunas ou tabelas diretamente no modelo do Power BI quebrarão as chamadas do HTML caso não haja governança de dados estruturada.
