# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 49 Python Brasil (J.Siqueira 04/22)."""

# Faça um programa que mostre os n termos da Série a seguir:

#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

# Imprima no final a soma da série.

import os

os.system("clear")

soma = 0
m = 1
a = ""
c = 40

print("=" * c)
print("SOMA TERMOS DA SEQUENCIA")
print("=" * c)

n = int(input("Digite um numero: "))

for n in range(1, n + 1):
    a += f"{n}/{m} + "
    soma += n / m
    m += 2

print(f"\nS: {a[:-3]} = \033[1;33m{soma:.2f}\033[1;m\n")


# ========================================
# SOMA TERMOS DA SEQUENCIA
# ========================================
# Digite um numero: 5

# S: 1/1 + 2/3 + 3/5 + 4/7 + 5/9 = 3.39
