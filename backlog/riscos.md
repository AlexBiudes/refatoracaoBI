# Riscos do Projeto

Abaixo estão descritos os principais riscos técnicos e funcionais identificados na etapa inicial de planejamento do projeto de Refatoração BI.

---

- **Risco 1**: API do Power BI não retornar todos os metadados necessários para mapear a posição exata e estilização detalhada de visuais.
- **Risco 2**: Medidas DAX complexas dependerem de um modelo semântico legado não documentado ou com regras embutidas difíceis de isolar.
- **Risco 3**: Falta de permissões administrativas no Power BI Service ou no Azure AD para registrar o Service Principal e obter tokens de acesso da API.
- **Risco 4**: Divergência técnica entre os visuais e fórmulas antigas e as regras reais homologadas pelo time de negócio (ex: bugs no dashboard original herdados na refatoração).
- **Risco 5**: Risco de perda de contexto e histórico do projeto caso a equipe de desenvolvimento ou as regras contábeis do ERP mudem no meio da execução.
- **Risco 6**: Risco de interpretação incorreta dos indicadores financeiros por parte dos agentes especialistas da equipe sem homologação constante de controladoria.
- **Risco 7**: Atraso no cronograma por gargalo no tempo de resposta do cliente para validação conceitual e de negócio de regras complexas (ex: critérios de rateio).
