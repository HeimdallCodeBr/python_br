# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 18 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que, dado um conjunto de N números, determine o menor
# valor, o maior valor e a soma dos valores.

import random

menor = 1000000000
maior = 0
soma = 0

print('\n')

for i in range(10):
    x = random.randint(0, 20)
    print(x, end=", ")
    soma += x

    if x < menor:
        menor = x
    if x > maior:
        maior = x


print("\n")
print(f"Valor menor: {menor}")
print(f"Valor maior: {maior}")
print(f"Soma: {soma}")
print('\n')
