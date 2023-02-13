# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 05 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

from os import system
from random import randint

system('clear')

vetor = []
v1 = []
v2 = []

for i in range(20):
    a = randint(1, 100)
    vetor.append(a)

    if vetor.index(a) % 2 == 0:
        v1.append(a)
    else:
        v2.append(a)

print(f'Vetor original: {vetor}\n')
print(f'Vetor 1.......: {v1}\n')
print(f'Vetor 2.......: {v2}\n')


# Vetor original: [86, 91, 9, 25, 74, 13, 50, 74, 28, 71, 48, 60, 39, 83, 48, 94, 16, 29, 74, 62]

# Vetor 1.......: [86, 9, 74, 50, 74, 28, 48, 39, 48, 16, 74]

# Vetor 2.......: [91, 25, 13, 71, 60, 83, 94, 29, 62]
