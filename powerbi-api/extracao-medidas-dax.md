# Extração de Medidas DAX

Estratégias e práticas para obtenção automatizada ou manual das fórmulas DAX declaradas no modelo semântico.

---

## Objetivo da Extração
Isolar e catalogar todas as medidas DAX vinculadas às telas EBITDA, Rentabilidade e Custos, mapeando sua sintaxe exata e dependências estruturais para replicação no modelo de consultas da nova solução.

## Estratégias Possíveis

### 1. Extração Automatizada via DMV (Dynamic Management Views)
- **Método**: Se houver acesso direto ao serviço do Power BI Premium via endpoint XMLA, realizar consultas SQL contra as DMVs do modelo tabular (Analysis Services).
- **Query Exemplo**:
  ```sql
  SELECT [MEASURE_NAME], [EXPRESSION], [DESCRIPTION], [TABLE_NAME] 
  FROM $SYSTEM.TMSCHEMA_MEASURES
  ```

### 2. Extração via Tabular Editor (Recomendado)
- **Método**: Abrir o arquivo de modelo (.pbix ou pasta do projeto TMDL) no utilitário de apoio técnico Tabular Editor (versão 2 ou 3) e exportar a lista de medidas em formato de planilha (CSV) ou script.

### 3. Extração via Power BI REST API (Limitações)
- **Método**: O endpoint tradicional de metadados da API de dataset não retorna a expressão da fórmula DAX por motivos de segurança do modelo intelectual. É necessário utilizar a API de administração do scanner (`GetScanResult`) para extrair a definição completa do modelo semântico, incluindo as expressões de medidas.

## Validação Manual e Registro das Medidas
- Após a extração por qualquer método, as medidas devem ser confrontadas com os relatórios em produção e catalogadas nas tabelas de documentação técnica do repositório em `telas-antigas/{tela}/medidas-dax.md`.
- Toda alteração ou otimização sugerida nas fórmulas DAX originais deve conter um registro de "Antes" e "Depois" bem especificado.
