# Navegação e Interatividade

Diretrizes de usabilidade para interação do usuário final com a aplicação web refatorada.

---

## Navegação entre Telas
- A transição entre os dashboards (EBITDA, Rentabilidade, Custos) será feita por meio de uma barra de navegação superior (Tabs) que altera dinamicamente o estado ativo sem recarregar a página inteira (Single Page Application - SPA behavior).
- O estado selecionado na URL deve persistir via query parameters (ex: `?screen=ebitda&year=2026`) para permitir o compartilhamento de links filtrados.

## Filtros Globais
- Toda alteração em segmentadores centrais (ex: alterar ano fiscal de 2025 para 2026) deve disparar um evento global que atualiza o modelo de dados dos gráficos ativos simultaneamente com animação suave de transição (fade-in/fade-out).

## Interações entre Gráficos (Cross-filtering)
- O clique em um elemento de barra de um gráfico (ex: clicar na barra do canal "E-commerce") deve atuar como filtro rápido, recalculando e filtrando as demais informações da tela apenas para a dimensão selecionada.
- Um botão de "Limpar Filtro Cruzado" deve aparecer flutuante quando houver um filtro de clique ativo na tela.

## Drill-Down
- Em gráficos de hierarquia (ex: Categoria de Custo > Conta Contábil), o clique duplo ou duplo toque (mobile) deve avançar para o próximo nível de detalhamento estrutural daquela categoria específica.

## Tooltips Customizados
- Rótulos informativos dinâmicos em hover contendo:
  - Título do ponto de dados selecionado.
  - Valor absoluto formatado na moeda local (BRL).
  - Variação percentual sobre a meta.
  - Linha auxiliar vertical de apoio para guiar a leitura do mouse.

## Estados Vazios (Empty States)
- Se a combinação de filtros selecionada pelo usuário não retornar dados no banco, exibir uma mensagem amigável no centro da tela ("Nenhum lançamento encontrado para a seleção de filtros atual") acompanhada de um botão rápido para resetar os filtros.
