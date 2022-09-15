# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 03 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


import os
from operator import index

os.system('clear')

nota = [7, 6.5, 7, 5]
media = 0

for i in nota:
    print(f'Nota: {i}')
    media += i
    media = media / 4

print('='*10)
print(f'Média: {media:.1f}\n')
