from os import system

import PyPDF2 as pyf

system('clear')


num_exercicios = 15
local = 'src/L05/'
arquivo_pdf = '05'


arquivo = pyf.PdfReader(f'{arquivo_pdf}.pdf')
num_paginas = len(arquivo.pages)

texto_pagina = ''
for pg in range(num_paginas):
    pagina = arquivo.pages[pg]
    texto_pagina += ''.join(pagina.extract_text())


remove_cab = texto_pagina.find('1.')
remove_rod = texto_pagina.find('Voltar para a', remove_cab)
texto_pagina = texto_pagina[remove_cab:remove_rod]
# texto_pagina = texto_pagina.replace('\n', '')
texto_pagina = texto_pagina.replace(' .', '. ')
texto_pagina = texto_pagina.replace(' ,', ', ')
texto_pagina = texto_pagina.replace('‘', '"')
texto_pagina = texto_pagina.replace('’', '"')
# print(texto_pagina)


for exercicio in range(1, num_exercicios):
    p_inicial = texto_pagina.find(f'{exercicio}. ')
    p_final = texto_pagina.find(f'{exercicio+1}. ', p_inicial)
    texto_exercicio = texto_pagina[p_inicial:p_final]
    with open(f'{local}L{str(exercicio).zfill(2)}.py', 'w') as saida:
        saida.write(f'# -*- coding: utf-8 -*-\n\n')
        saida.write(
            f'"""Resolução Lista {arquivo_pdf} Exercicio {str(exercicio).zfill(2)} Python Brasil (J.Siqueira 02/23)."""\n\n')
        saida.write(f'"""\n{texto_exercicio}"""\n')
