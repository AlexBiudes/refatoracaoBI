# Agentes Autônomos Antigravity

Este diretório armazena os prompts do sistema e as atribuições de tarefas para a equipe de agentes de inteligência artificial autônomos que operam na plataforma Antigravity.

---

## Objetivo dos Agentes
O conjunto de agentes atua em cooperação técnica para mapear as telas legadas do Power BI, validar regras de negócio, modelar e otimizar medidas DAX, definir padrões de interface frontend (HTML/CSS) e testar a qualidade final do projeto.

## Ordem Sugerida de Execução
Para garantir o fluxo correto de dependências lógicas no projeto:
1. **00-orquestrador**: Define o escopo e coordena as chamadas.
2. **01-agente-arquiteto-projeto**: Organiza a infraestrutura de diretórios e padrões.
3. **02-agente-mapeador-powerbi** & **03-agente-especialista-dax**: Conduzem a extração técnica inicial.
4. **04-agente-ux-ui**: Projeta o redesign visual baseado nas deficiências detectadas pelo mapeador.
5. **05-agente-front-end-html**: Recebe as definições visuais e cria os templates HTML.
6. **06-agente-validador-negocio** & **07-agente-qa**: Homologam os dados e testam o frontend.
7. **08-agente-documentador**: Mantém a base de documentação atualizada em todas as etapas.

## Como Usar os Prompts
- Cada arquivo markdown neste diretório (`00-orquestrador.md` a `08-agente-documentador.md`) contém a definição do prompt do sistema para aquele agente específico.
- Ao inicializar um novo subagente ou delegar tarefas, use a instrução descrita como contexto base ou system prompt da conversação.

## Regra de Não Alterar Arquivos Fora do Escopo
- Nenhum agente está autorizado a editar, mover ou deletar arquivos fora do diretório do projeto `refatoracaoBI/` sem autorização explícita registrada nas decisões do projeto.

## Regra de Sempre Validar Antes de Sobrescrever
- Antes de aplicar alterações em arquivos de documentação ou código existentes, o agente deve ler o arquivo atual, comparar a mudança planejada e realizar o merge seguro de informações para evitar perda de dados históricos do mapeamento.
