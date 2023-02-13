# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 50 Python Brasil (J.Siqueira 04/22)."""

# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 

# Faça um programa que calcule o valor de H com N termos.

import os
os.system('clear')

soma = 0
m = 1
a = ""
c = 40

print("=" * c)
print("SOMA TERMOS DA SEQUENCIA")
print("=" * c)

n = int(input("Digite um numero: "))

for n in range(1, n + 1):
    a += f"{m}/{n} + "
    soma += 1 / n
    

print(f"\nS: {a[2:-3]} = \033[1;33m{soma:.2f}\033[1;m\n")


