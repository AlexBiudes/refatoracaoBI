# Padrões de Documentação

Para garantir a consistência e clareza de todas as informações geradas neste projeto, definimos as seguintes regras de formatação, tabelas e estruturas.

---

## 1. Títulos e Hierarquia

- Use títulos expressivos utilizando `#` (H1) apenas para o título principal da página.
- Subseções devem utilizar `##` (H2) e tópicos específicos `###` (H3).
- Mantenha a nomenclatura de arquivos em minúsculas com hífen para separação (ex: `mapeamento-geral.md`).

## 2. Tabelas Padrão

### Cadastro de Medidas DAX
```markdown
| Nome da Medida | Fórmula DAX | Tabela de Origem | Objetivo do Indicador | Status |
|---|---|---|---|---|
| `[Exemplo Medida]` | `SUM(Tabela[Valor])` | `Tabela` | Descrição sucinta. | [Pendente / Validada] |
```

### Cadastro de Gráficos e Visuais
```markdown
| ID Visual | Tipo de Visual | Indicador Principal | Eixos / Dimensões | Valores / Métricas | Observações / Interações |
|---|---|---|---|---|---|
| V01 | Gráfico de Linha | EBITDA Mensal | Eixo X: Calendário[Mês-Ano] | Eixo Y: `[Margem EBITDA]` | Drill-down habilitado para dia. |
```

### Registro de Decisões do Projeto
```markdown
| ID | Data | Decisão Tomada | Motivo / Justificativa | Impacto no Projeto | Responsável |
|---|---|---|---|---|---|
| D01 | DD/MM/AAAA | Uso de Vanilla CSS | Evitar complexidade de compilação. | Layout modular sem dependências. | Alex Biudes |
```

## 3. Uso de Checklists e Status

Para checklists de tarefas e validações de itens, utilize:
- `[ ]` Item não iniciado / pendente.
- `[/]` Item em desenvolvimento ou validação parcial.
- `[x]` Item concluído e verificado.

## 4. Campos Obrigatórios na Análise de Telas

Ao descrever qualquer visual nas pastas de mapeamento, é obrigatório registrar:
1. **Nome Técnico**: O nome exato que aparece no metadados da API (se aplicável).
2. **Propósito de Negócio**: Qual dor do usuário esse gráfico específico resolve.
3. **Métrica Principal**: Qual medida DAX é utilizada no campo de valores.
4. **Filtros Aplicados**: Se há filtros específicos no nível do visual que alteram o cálculo padrão da medida.

## 5. Linguagem e Tom

- A documentação deve ser redigida em **português brasileiro (pt-BR)**.
- Adote um tom formal, objetivo e técnico.
- Evite adjetivos vagos. Prefira dados analíticos claros e específicos (ex: em vez de "painel lento", use "tempo de renderização de visual superior a 5 segundos").
