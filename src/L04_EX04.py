# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 04 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
# consoantes foram lidas. Imprima as consoantes.

from os import system

system('clear')

a = ['b', 'e', 'a', 'f', 'u', 'g', 'i', 'h', 't', 'z']

print(f'Vetor original..............: {a}\n')

contar = 0
consoantes = ''

for i in a:
    if i not in "aeiou":
        contar += 1
        consoantes += f'{i}, '

print(f'Total de consoantes lidas...: {contar}\n')
print(f'Consoantes..................: {consoantes[:-2:]}\n')


# Vetor original..............: ['b', 'e', 'a', 'f', 'u', 'g', 'i', 'h', 't', 'z']

# Total de consoantes lidas...: 6

# Consoantes..................: b, f, g, h, t, z
