# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 19 Python Brasil (J.Siqueira 03/21)."""

# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

import random

menor = 10000
maior = 0
soma = 0

print('\n')

for i in range(10):
    x = random.randint(0, 1000)
    
    soma += x

    if x < menor:
        menor = x
    if x > maior:
        maior = x
    print(x, end=", ")

print("\n")
print(f"Valor menor: {menor}")
print(f"Valor maior: {maior}")
print(f"Soma: {soma}")
print('\n')

