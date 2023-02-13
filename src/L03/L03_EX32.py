# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 32 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que calcule o fatorial de um número inteiro
# fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme
# o exemplo abaixo: 

# Fatorial de: 5
# 5! = 5 . 4 . 3 . 2 . 1 = 120

import os

os.system('clear')

n = int(input('Informe o numero para gera fatorial: '))
f = 1
c = ''

for i in reversed(range(1, n+1)):
    f *= i
    c += str(i) + ' . '   
print(f'\n{n}! = {c[:-2]}= {f}\n\n', end='')
