import PyPDF2
import sys

reader = PyPDF2.PdfReader(r'c:\Users\alex.biudes\Desktop\Documentação\MCP\3telas\Gabarito.pdf')
print(f'Total de paginas: {len(reader.pages)}')
for i in range(len(reader.pages)):
    print(f'\n=== PAGINA {i+1} ===')
    text = reader.pages[i].extract_text()
    if text:
        print(text)
    else:
        print('[Sem texto extraivel - possivelmente imagem]')
