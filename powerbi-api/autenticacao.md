# Autenticação

Especificação técnica para o fluxo de autenticação e geração de tokens de acesso à API REST do Power BI.

---

## Azure Active Directory (Azure AD) / Entra ID
- A autenticação fará uso do portal Azure Active Directory como provedor de identidade.
- Será criado um registro de aplicativo (App Registration) representando a aplicação de refatoração BI.

## Service Principal (Entidade de Serviço)
- Fluxo de concessão de credenciais de cliente OAuth 2.0 (`client_credentials`).
- O aplicativo de refatoração autentica-se diretamente contra o endpoint do Azure AD utilizando:
  - **Tenant ID**: Identificador do locatário Microsoft.
  - **Client ID**: Identificador exclusivo do aplicativo registrado.
  - **Client Secret**: Chave secreta de autenticação de aplicação.

## Permissões (API Permissions)
- As seguintes permissões delegadas ou de aplicativo do Power BI Service devem ser configuradas no Azure AD:
  - `Report.Read.All`
  - `Dataset.Read.All`
  - `Workspace.Read.All`

## Geração do Token de Acesso (Access Token)
- O backend intermediário da aplicação realiza um POST para:
  `POST https://login.microsoftonline.com/{tenantId}/oauth2/v2.0/token`
- Payload da requisição:
  ```text
  grant_type=client_credentials
  client_id={clientId}
  client_secret={clientSecret}
  scope=https://analysis.windows.net/powerbi/api/.default
  ```
- O token JWT recebido no retorno da API Microsoft possui expiração padrão de 1 hora e deve ser incluído no cabeçalho das chamadas à API do Power BI:
  `Authorization: Bearer {accessToken}`

## Variáveis de Ambiente e Boas Práticas
- As credenciais de Tenant, Client e Secret devem ser armazenadas exclusivamente como variáveis de ambiente (.env) no servidor de hospedagem backend.
- Nunca escreva credenciais em arquivos de código frontend ou repositórios públicos do GitHub.
