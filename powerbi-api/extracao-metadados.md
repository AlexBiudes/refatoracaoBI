# Extração de Metadados

Metodologia e script conceitual para extração das definições de componentes e estruturas lógicas dos relatórios e conjuntos de dados mapeados.

---

## Metadados do Relatório e Páginas
A API REST permite retornar o JSON contendo os nomes das abas e a disposição interna dos elementos visuais. A leitura destes metadados ajuda a mapear:
- Lista de páginas ativas e ocultas.
- Posição (coordenadas X, Y, largura, altura) e tipo de cada gráfico (barra, linha, matriz) na tela de origem.

## Metadados do Dataset (Modelo Semântico)
Permite extrair as definições lógicas das tabelas que compõem o modelo de dados:
- Nomes das tabelas e tipos de dados de cada coluna.
- Chaves primárias e estrangeiras de relacionamentos lógicos (ex: Fato_Faturamento -> Dim_Calendario).
- Descrições internas de campos de metadados.

## Ferramenta de Extração Recomendada
- Utilização de scripts baseados em PowerShell (módulo `MicrosoftPowerBIMgmt`) ou scripts Python (biblioteca `requests`) para automatizar as requisições recursivas.

## Exemplo de Resposta de Metadados de Visual (Conceitual)
```json
{
  "name": "Visual_Evolucao_Ebitda",
  "type": "lineChart",
  "title": "Evolução Mensal do EBITDA",
  "layout": {
    "x": 20,
    "y": 140,
    "width": 640,
    "height": 320
  },
  "queryFields": [
    "Dim_Calendario.Mes_Ano",
    "Fato_Lancamentos.EBITDA"
  ]
}
```

## Limitações Conhecidas
- A estrutura de layout detalhada (cores exatas, fontes, espessuras de bordas) não é retornada pelos endpoints padrão da API de visual, exigindo inspeção manual complementar na ferramenta desktop do Power BI.
