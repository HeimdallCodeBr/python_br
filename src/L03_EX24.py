# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 24 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que calcule o mostre a média aritmética de N notas.

import os
os.system('clear')

t = int(input('Informe o numero de termos: '))
print('\n')
s = 0
for i in range(t):
    v = int(input(f'Informe valor para termo {i+1}: '))
    s += v
print(f'\nMédia: {(s/t):.2f}\n')
