import os
os.system('clear')

# Crie um código que conta o número de vogais de um bloco de texto qualquer.
# O código deve desconsiderar letras maiúsculas/minúsculas, isto é, "a" e "A" contam da mesma forma.
# O texto pode ser colado diretamente como um string no código.

texto = """
Python é uma linguagem de programação de alto nível,[5] interpretada de script,
imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. 
Foi lançada por Guido van Rossum em 1991.[1] Atualmente, possui um modelo de 
desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos
Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e
especificações formais, a linguagem, como um todo, não é formalmente especificada.
O padrão na pratica é a implementação CPython. A linguagem foi projetada com a filosofia
de enfatizar a importância do esforço do programador sobre o esforço computacional. 
Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe
concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks
desenvolvidos por terceiros.  Python é uma linguagem de propósito geral de alto nível, 
multiparadigma, suporta o paradigma orientado a objetos, imperativo, funcional e procedural.
Possui tipagem dinâmica e uma de suas principais características é permitir a fácil leitura 
do código e exigir poucas linhas de código se comparado ao mesmo programa em outras linguagens.
Devido às suas características, ela é utilizada, principalmente, para processamento de textos,
dados científicos e criação de CGIs para páginas dinâmicas para a web. Foi considerada pelo 
público a 3ª linguagem "mais amada", de acordo com uma pesquisa conduzida pelo site Stack 
Overflow em 2018[6] e está entre as 5 linguagens mais populares, de acordo com uma pesquisa 
conduzida pela RedMonk.[7] O nome Python teve a sua origem no grupo humorístico britânico Monty
Python,[8] criador do programa Monty Python's Flying Circus, embora muitas pessoas façam associação
com o réptil do mesmo nome (em português, píton ou pitão).
"""

texto = texto.replace(' ','')
texto = texto.lower()

# criterio = {
#     'a'   : 'aáâàä',
#     'e'   : 'eéêèë',
#     'i'   : 'iíîìï',
#     'o'   : 'oóôòö',
#     'u'   : 'uúûùü',
# }

# for chave, valor in criterio.items():
#     for letra_acento in valor:
#         for letra in texto:
#             if letra == letra_acento:
#                 texto = texto.replace(letra, chave)

print (f'A - {texto.count('a')}')
print (f'E - {texto.count('e')}')
print (f'I - {texto.count('i')}')
print (f'O - {texto.count('o')}')
print (f'U - {texto.count('u')}')








