# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 10 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão
# ser compostos pelos elementos intercalados dos dois outros vetores.

from os import system

system('clear')

v0 = ['73', '81', '22', '35', '01', '21', '23', '56', '31', '26']
v1 = ['63', '14', '75', '43', '88', '88', '44', '78', '73', '97']
v2 = []
m = 0
n = 0

s = len(v0+v1)

print(f'v0: {v0}')
print(f'v1: {v1}')
print('\n')

for i in range(s):
    if i % 2 == 0:
        v2.append(v0[m])
        m += 1
    else:
        v2.append(v1[n])
        n += 1

print(f'v2: {v2}')
