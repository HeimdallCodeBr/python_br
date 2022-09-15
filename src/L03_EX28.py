# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 28 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que calcule o valor total investido por um colecionador
# em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário
# deverá informar a quantidade de CDs e o valor para em cada um.

import os

os.system('clear')

q = int(input('Informe a quantidade de CD: '))
print('\n')
soma = 0

for i in range(q):
    v = float(input(f'Informe o valor do CD{i+1}: '))
    soma += v
print('\n')
print('='*50)
print(f'Valor total do investimento em CD\'s é {soma:.2f}R$ ')
print('='*50)