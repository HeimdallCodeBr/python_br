# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 14 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que peça 10 números inteiros, calcule e mostre
# a quantidade de números pares e a quantidade de números impares.

p, i = 0, 0

for k in range(10):
    n = int(input(f"Informe {k+1}º numero: "))

    if n % 2 == 0:
        p += 1
    else:
        i += 1

print(f"\nTotal de numeros impares {i}, Total de numeros pares {p}\n")
