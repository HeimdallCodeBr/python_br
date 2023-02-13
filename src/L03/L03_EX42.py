# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 42 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que leia uma quantidade indeterminada de números positivos
# e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75]
# e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

import os, random
os.system('clear')

lista = []
a_025 = 0
b_050 = 0
c_075 = 0
d_100 = 0

for i in range(100):
    x =  random.randrange(0,100)
    lista.append(x)

for k in range(len(lista)):
    if lista[k] >= 0 and lista[k] <= 25:
        a_025 += 1
    if lista[k] >= 26 and lista[k] <= 50:
        b_050 += 1
    if lista[k] >= 51 and lista[k] <= 75:
        c_075 += 1
    if lista[k] >= 76 and lista[k] <= 100:
        d_100 += 1

    
print('Distribuição Amostras')
print('\n')
print(lista)
print('\n')
print('-'*70)
print(f'[0-25]\t\t| [26-50]\t| [51-75]\t | [76-100]')
print('-'*70)
print(f'{a_025}\t\t| {b_050}\t\t| {c_075}\t\t | {d_100}')
print('-'*70)
print('\n')
print(f'Total de amostras agrupadas: {a_025+b_050+c_075+d_100}')
print('\n')


# Distribuição Amostras


# [63, 17, 11, 94, 2, 9, 93, 99, 71, 83]


# ----------------------------------------------------------------------
# [0-25]          | [26-50]       | [51-75]        | [76-100]
# ----------------------------------------------------------------------
# 4               | 0             | 2              | 4
# ----------------------------------------------------------------------


# Total de amostras agrupadas: 10
