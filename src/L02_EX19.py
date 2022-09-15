# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 19 Python Brasil (J.Siqueira 03/21)."""

# Faça um Programa que leia um número inteiro menor que 1000 e imprima a
# quantidade de centenas, dezenas e unidades do mesmo. Observando os termos
# no plural a colocação do "e", da vírgula entre outros.
# Exemplo:326 = 3 centenas, 2 dezenas e 6 unidades
#               12 = 1 dezena e 2 unidades
#
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21,
#             11, 1, 7 e 16


n = str(input("\nDigite numero entre 0 - 999: "))

a = len(n)
c_s = 's'
d_s = 's'
u_s = 's'

if a == 3:
    if n[0] == '1':
        c_s = ''
        if n[1] == '1':
            d_s = ''
            if n[2] == '1':
                u_s = ''
    print(f'{n[0]} centena{c_s}, {n[1]} dezena{d_s} e {n[2]} unidade{u_s}.')
elif a == 2:
    if n[0] == '1':
        d_s = ''
        if n[1] == '1':
            u_s = ''
    print(f'{n[0]} dezena{d_s} e {n[1]} unidade{u_s}.')
elif a == 1:
    if n[0] == '1':
        u_s = ''
    print(f'{n[0]} unidade{u_s}.')
else:
    (print('Valor inválido!'))
