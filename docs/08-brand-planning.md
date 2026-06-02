# Brand Planning — Diretrizes para Telas HTML do BI Performance
 
> Documento de governança visual para orientar a prototipagem e implementação das telas HTML do BI Performance dentro da identidade da Planning.
>
> Fonte de referência: Planning Brand Book — Manual de Identidade Visual — Versão 1.0.
 
## 1. Objetivo
 
Este documento traduz a identidade visual oficial da Planning para a POC de refatoração das telas do BI Performance em HTML.
 
Toda nova tela HTML deve respeitar esta linguagem visual, salvo exceção explicitamente documentada.
 
## 2. Essência da marca
 
A marca combina um símbolo radial com o nome Planning em tipografia sem serifa, geométrica e de cantos suaves.
 
O símbolo representa expansão, energia e movimento a partir de um centro. Nas telas analíticas, isso deve aparecer como clareza visual, direção executiva, sensação de crescimento e leitura limpa dos números.
 
## 3. Tagline oficial
 
```text
Building your company's future. Today.
```
 
Diretrizes:
 
- usar principalmente em capas, divisórias, telas institucionais ou estados de abertura;
- destacar `Today.` em verde e peso mais forte quando a tagline for reproduzida;
- em telas analíticas densas, a tagline pode ser discreta ou omitida para priorizar os dados.
 
## 4. Logotipo e símbolo
 
Versões oficiais:
 
- principal para fundo claro: símbolo verde e texto preto;
- principal para fundo escuro: símbolo verde e texto branco;
- monocromática preta para fundo claro sem cor;
- monocromática branca para fundo escuro sem cor.
 
Regras:
 
- priorizar a versão colorida;
- não distorcer, esticar, girar ou recolorir;
- preservar área de respiro;
- em telas, manter largura mínima aproximada de 120 px quando o nome Planning estiver visível;
- posicionar discretamente, normalmente no canto superior ou inferior direito;
- o símbolo isolado pode ser usado como marca d'água, selo ou elemento gráfico secundário.
 
## 5. Paleta de cores oficial
 
| Token | HEX | Uso recomendado |
|---|---:|---|
| Verde Planning | `#0AE18C` | Cor primária, destaques, linhas e estados positivos |
| Verde escuro | `#00BF63` | Apoio, textos em fundos claros e variações de destaque |
| Ciano | `#14C8FA` | Detalhes, destaques secundários e gradientes |
| Preto | `#000000` | Fundos escuros, textos fortes e estrutura |
| Branco | `#FFFFFF` | Fundo principal, cards e áreas de leitura |
| Cinza claro | `#F2F2F2` | Fundo auxiliar e separadores suaves |
| Verde suave | `#C9F7E2` | Caixas de considerações e leitura analítica |
| Vermelho alerta | `#FF3131` | Indicadores negativos e alertas críticos |
 
Diretrizes:
 
- o verde Planning é assinatura, não fundo dominante de tela inteira;
- ciano é apoio visual;
- vermelho somente para negativos, alertas ou exceções;
- telas analíticas devem priorizar leitura limpa, contraste e espaço livre.
 
## 6. Tipografia
 
A tipografia oficial é Poppins.
 
| Uso | Peso recomendado |
|---|---|
| Títulos e destaques | Poppins Bold |
| Subtítulos | Poppins Medium |
| Texto corrido | Poppins Light |
| Labels e metadados | Poppins Light ou Medium |
| KPIs numéricos | Poppins Bold ou Medium |
 
Fallbacks permitidos:
 
```css
font-family: 'Poppins', 'Montserrat', 'Open Sans', Arial, sans-serif;
```
 
Na POC do Power BI, evitar dependência de Google Fonts ou CDN. Se a fonte não estiver disponível, usar fallback local.
 
## 7. Aplicação em telas HTML
 
Diretrizes visuais:
 
- visual limpo, tecnológico e contemporâneo;
- bastante espaço livre;
- cards brancos ou superfícies escuras com contraste consistente;
- verde e ciano como acentos, não preenchimentos dominantes;
- vermelho apenas em alertas ou indicadores negativos;
- linha de destaque em gradiente verde para ciano;
- caixas de considerações em verde suave quando houver leitura analítica;
- hierarquia forte para KPIs, gráficos e rankings.
 
## 8. Estrutura recomendada para dashboards
 
```text
Header executivo
        ↓
Linha de destaque verde para ciano
        ↓
Cards principais de KPI
        ↓
Gráfico ou bloco analítico principal
        ↓
Tabela, ranking ou composição
        ↓
Caixa de considerações ou alertas, quando aplicável
```
 
## 9. O que evitar
 
Evitar:
 
- visual genérico de template SaaS sem identidade Planning;
- neon excessivo;
- fundos verdes chapados em tela inteira;
- excesso de sombras, brilhos ou efeitos 3D;
- contraste baixo;
- vermelho para destaque comum;
- filtros globais funcionais dentro do HTML;
- dependência de bibliotecas externas sem justificativa;
- elementos que não ajudem a leitura analítica.
 
## 10. Aplicação na Tela 001
 
Para a tela 001, o protótipo deve ser revisado à luz desta brand.
 
Pontos de atenção:
 
- o protótipo atual pode estar mais próximo de uma estética dark tech/neon e deve ser reavaliado;
- a versão final deve se aproximar da identidade Planning: limpa, tecnológica, contemporânea e com espaço livre;
- verde Planning deve ser assinatura visual;
- ciano deve apoiar curva, detalhes e gradientes;
- vermelho apenas para alertas;
- Poppins ou fallback sem serifa;
- o simulador de contexto permanece apenas no protótipo estático, não na medida HTML final.
 
## 11. Critérios de aceite visual
 
Uma tela HTML será considerada aderente à brand quando:
 
- respeitar a paleta oficial;
- usar tipografia compatível com Poppins;
- tiver hierarquia clara;
- usar verde como assinatura, não como fundo dominante;
- usar vermelho apenas para indicadores negativos;
- preservar leitura executiva dos KPIs;
- manter visual limpo, tecnológico e contemporâneo;
- documentar qualquer exceção estética aplicada à tela.
