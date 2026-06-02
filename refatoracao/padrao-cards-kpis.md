# Padrão de Cards e KPIs

Especificação padrão para exibição unificada dos indicadores-chave de desempenho em todas as telas.

---

## Estrutura do Padrão dos Cards

Cada card de KPI deve conter obrigatoriamente os seguintes elementos visuais e de dados:

1. **Nome do Indicador**: Texto curto em caixa alta identificando a métrica (ex: `MARGEM EBITDA`).
2. **Valor Principal**: Valor numérico em destaque (ex: `R$ 4.25M` ou `35.2%`).
3. **Variação (Badge de Tendência)**: Badge colorido com a variação percentual em relação ao mês anterior (MoM) ou ano anterior (YoY):
   - **Verde**: Indica variação positiva em receitas/lucros ou variação negativa (economia) em despesas/custos.
   - **Vermelho**: Indica queda em receitas/lucros ou estouro em despesas/custos.
4. **Comparação de Referência**: Texto secundário de suporte indicando o valor de comparação (ex: `vs. R$ 4.10M no Planejado`).
5. **Ícone Opcional**: Ícone representativo no canto superior direito para apoio à identificação rápida (ex: cifrão, gráfico de alta, carrinho de compras).
6. **Status Visual**: Borda fina ou detalhe de linha colorida na parte inferior do card indicando se o resultado geral está "Dentro da Meta", "Em Atenção" ou "Crítico".
7. **Observação de Tooltip**: Pequeno ícone de ajuda `(?)` que exibe a definição do glossário e a fórmula de cálculo ao passar o mouse.
