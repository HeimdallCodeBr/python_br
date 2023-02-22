from os import system

import PyPDF2 as pdf

system('clear')
arquivo = pdf.PdfReader('script/extrai_img_pdf/tm.pdf')

num_pagina = len(arquivo.pages)
c = 0
for i in range(num_pagina):
    pagina = arquivo.pages[i]
    print(
        f'Processo de extração andamento...{i+1}/{num_pagina}\r', end='')
    for img in pagina.images:
        n = f'script/extrai_img_pdf/img/{img.name}'
        with open(n, 'wb') as saida:
            saida.write(img.data)
            c += 1
print('\nConcluido com sucesso!')
