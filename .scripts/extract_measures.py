import sys
import re

def parse_tmdl(filepath, filter_keywords=None):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match 'measure <name> = <formula>' or 'measure <name> = ``` <formula> ```'
    # Actually, the file format is:
    # 	measure Vendas_Mes_Atual = ```
    # 			<formula>
    # 			```
    # 		formatString: "R$"\ #,0;-"R$"\ #,0;"R$"\ #,0
    # or
    # 	measure %margem_lucro_por_produto =
    # 			<formula>
    # 		formatString: 0.00%;-0.00%;0.00%
    
    # We can split by "\n\tmeasure " to get each measure block
    blocks = content.split('\n\tmeasure ')
    
    measures = []
    
    for block in blocks[1:]:
        # first line contains the measure name and the start of the formula
        lines = block.split('\n')
        first_line = lines[0]
        
        # 'Name = ...'
        if ' = ' in first_line:
            name, rest = first_line.split(' = ', 1)
        else:
            name = first_line.strip()
            rest = ""
            
        formula_lines = []
        if rest.startswith('```'):
            # multi-line formula until next ```
            in_code = True
            for line in lines[1:]:
                if line.strip() == '```':
                    break
                formula_lines.append(line)
        else:
            # formula continues until a line that starts with '\t\t' or empty
            formula_lines.append(rest)
            for line in lines[1:]:
                if line.startswith('\t\t') and ('formatString:' in line or 'lineageTag:' in line or 'annotation ' in line):
                    break
                formula_lines.append(line)
                
        formula = '\n'.join(formula_lines).strip()
        
        # check filters
        if filter_keywords:
            name_lower = name.lower()
            if not any(kw in name_lower for kw in filter_keywords):
                continue
                
        measures.append((name, formula))
        
    return measures

def generate_markdown(measures, title):
    md = f"# Medidas DAX — {title}\n\n"
    md += "## Medidas Extraídas do Modelo\n\n"
    md += "| Nome da Medida | Fórmula DAX | Objetivo | Status |\n"
    md += "|---|---|---|---|\n"
    
    for name, formula in measures:
        # escape backticks and newlines in formula for markdown table
        # We'll use <br> for newlines and escape pipe characters.
        clean_formula = formula.replace('\n', '<br>').replace('|', '&#124;').replace('`', '\\`')
        md += f"| `{name}` | `{clean_formula}` | - | Extraído |\n"
        
    return md

if __name__ == '__main__':
    mode = sys.argv[1]
    
    if mode == 'custos':
        filepath = r'c:\Users\alex.biudes\Desktop\Documentação\MCP\3telas\.tmdl-export\tables\medidas__relatorio_custos.tmdl'
        measures = parse_tmdl(filepath)
        md = generate_markdown(measures, "Variação dos Custos")
        out_path = r'c:\Users\alex.biudes\Desktop\Documentação\MCP\3telas\telas-antigas\variacao-custos\medidas-dax.md'
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"Escreveu {len(measures)} medidas em {out_path}")
        
    elif mode == 'ebitda':
        filepath = r'c:\Users\alex.biudes\Desktop\Documentação\MCP\3telas\.tmdl-export\tables\Medidas_balancetenew.tmdl'
        keywords = ["ebitda", "dre", "receita", "custo", "margem", "despesa"]
        measures = parse_tmdl(filepath, keywords)
        md = generate_markdown(measures, "EBITDA")
        out_path = r'c:\Users\alex.biudes\Desktop\Documentação\MCP\3telas\telas-antigas\ebitda\medidas-dax.md'
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"Escreveu {len(measures)} medidas em {out_path}")
        
    elif mode == 'rentabilidade':
        filepath = r'c:\Users\alex.biudes\Desktop\Documentação\MCP\3telas\.tmdl-export\tables\Medidas_balancetenew.tmdl'
        keywords = ["rentabilidade", "lucratividade", "margem", "receita_liq"]
        measures = parse_tmdl(filepath, keywords)
        md = generate_markdown(measures, "Análise de Rentabilidade")
        out_path = r'c:\Users\alex.biudes\Desktop\Documentação\MCP\3telas\telas-antigas\analise-rentabilidade\medidas-dax.md'
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"Escreveu {len(measures)} medidas em {out_path}")
