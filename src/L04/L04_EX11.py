# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 11 Python Brasil (J.Siqueira 04/22)."""

# Altere o programa anterior, intercalando 3 vetores de
# 10 elementos cada.

from os import system

system('clear')

v0 = ['73', '81', '22', '35', '01', '21', '23', '56', '31', '26']
v1 = ['63', '14', '75', '43', '88', '88', '44', '78', '73', '97']
v2 = ['22', '05', '58', '85', '95', '71', '89', '07', '43', '70']
v3 = []

m = 0
n = 0
j = 0
i = 0
s = len(v0+v1+v2)

print(f'v0: {v0}')
print(f'v1: {v1}')
print(f'v2: {v2}')
print('\n')

while i < s:
    v3.insert(i, v0[m])
    m += 1
    i += 1

    v3.insert(i, v1[n])
    n += 1
    i += 1

    v3.insert(i, v2[j])
    j += 1
    i += 1

print(f'v3: {v3}')
