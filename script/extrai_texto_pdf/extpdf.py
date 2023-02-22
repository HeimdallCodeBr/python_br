from os import system

import PyPDF2 as pyf

system('clear')

# Informações de entrada quantidade de exercicio por lista,
# local destino dos arquivos de saida e numero da lista de exercicio
num_exercicios = 3
local = 'src/L09/'
arquivo_pdf = '09'
num_exercicios = num_exercicios + 1

# Le o arquivo .pdf utilizando o metodo PdfReader
arquivo = pyf.PdfReader(f'{arquivo_pdf}.pdf')
# Conta o numero de paginas do documento
num_paginas = len(arquivo.pages)

# Percorrer e extrair as paginas do documento
texto_pagina = ''
for pg in range(num_paginas):
    pagina = arquivo.pages[pg]
    texto_pagina += ''.join(pagina.extract_text())  # junta todas as paginas

# Tratamento do texto
# (remove cabeçalho e rodapé, espaços em branco, corrige pontuação)
remove_cab = texto_pagina.find('1.')
remove_rod = texto_pagina.find('Voltar para a', remove_cab)
texto_pagina = texto_pagina[remove_cab:remove_rod]
texto_pagina = texto_pagina.replace(' .', '. ')
texto_pagina = texto_pagina.replace(' ,', ', ')
texto_pagina = texto_pagina.replace('‘', '"')
texto_pagina = texto_pagina.replace('’', '"')

# Extrair cada exercicio
for exercicio in range(1, num_exercicios):
    p_inicial = texto_pagina.find(f'{exercicio}. ')
    p_final = texto_pagina.find(f'{exercicio+1}. ', p_inicial)
    texto_exercicio = texto_pagina[p_inicial:p_final]
# Cria um arquivo .py com cada exercicio extraido
    numero_arq = str(exercicio).zfill(2)
    with open(f'{local}L{numero_arq}.py', 'w') as saida:
        saida.write('# -*- coding: utf-8 -*-\n\n')
        saida.write(
            f'"""Resolução Lista {arquivo_pdf} Exercicio {numero_arq} Python Brasil (J.Siqueira 02/23)."""\n\n')
        saida.write(f'"""\n{texto_exercicio}"""\n')
