# Antigravity — Agente e Subagentes

A orquestração das tarefas deste projeto é conduzida pelo **Antigravity**, o agente principal autônomo baseado no Gemini.

Ao contrário de abordagens que exigem múltiplos prompts extensos colados manualmente no chat (ex: um prompt para o "Arquiteto", outro para o "Mapeador DAX", etc.), este projeto utiliza a arquitetura nativa de **subagentes do Antigravity**.

## Dinâmica de Execução

1. **Agente Principal**: O orquestrador central que recebe a diretriz (via documento como o `prompt_proxima_conversa.md`).
2. **Subagentes**: Quando o volume de trabalho excede a capacidade de atenção pontual (ex: analisar centenas de medidas DAX) ou exige atividades em paralelo (auditorias massivas de arquivos), o agente principal dispara subagentes (`research`, `self`, etc.) para analisar arquivos no background e consolidar a informação.
3. **Ferramentas Integradas**: O agente usa MCP, Git, PowerShell e scripts Python autonomamente, sem intervenção humana, comunicando os resultados após a conclusão.

Os prompts fixos manuais que existiam nesta pasta foram descontinuados por se tornarem obsoletos diante da gestão automática de contexto do Antigravity.
