# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 7 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que leia 5 números e informe o maior número.


m = 0

for i in range(1, 6):
    n = int(input(f"\nInforme {i}º numero: "))

    if n > m:
        m = n

print(f"\nO maior numero digitado foi {m}\n")
