import os
root = r'c:\Users\alex.biudes\Desktop\Documentação\MCP\3telas'
dirs_to_check = ['telas-antigas', 'docs', 'refatoracao', 'powerbi-api', 'antigravity', 'html-final', 'backlog']

for d in dirs_to_check:
    path = os.path.join(root, d)
    if not os.path.exists(path): continue
    for dp, dn, filenames in os.walk(path):
        for f in filenames:
            if f.endswith('.md'):
                filepath = os.path.join(dp, f)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if 'A ser preenchido' in content or 'A definir' in content or '[ ]' in content:
                        print(f'TEMPLATE_PLACEHOLDERS_FOUND: {filepath.replace(root, "")}')
