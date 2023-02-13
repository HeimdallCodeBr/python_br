"""Resolução Lista 02 Exercicio 10 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios

# Faça um Programa que pergunte em que turno você estuda. Peça para digitar
# M-matutino ou V-Vespertino ou N- Noturno.

# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
# "Valor Inválido!", conforme o caso.


p = input('Qual turno você estuda? [M]atutino, [V]espertino, [N]oturno: ')

if p in 'Mm':
    print('Bom dia!')
elif p in 'Vv':
    print('Boa Tarde!')
elif p in 'Nn':
    print('Boa Noite!')
else:
    print('Valor Inválido!')
