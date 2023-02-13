# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 17 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que calcule o fatorial de um número inteiro
# fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

# n	    n!
# 0 	1
# 1     1
# 2     2
# 3     6
# 4     24
# 5     120
# 6     720
# 7     5.040
# 8     40.320
# 9     362.880
# 10    3.628.800


n = int(input('\nInforme um numero: '))
f = 1

for i in range(2, n + 1):
    f = f * i
print(f'\033[1;32mFatorial [{n}!]: {f}\033[1;m\n')
