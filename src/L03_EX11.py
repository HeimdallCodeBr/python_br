# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 11 Python Brasil (J.Siqueira 03/21)."""

# Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Informe o 1º numero: "))
n2 = int(input("Informe o 2º numero: "))
s = 0

for i in range(n1, n2 + 1):
    print(i)
    s += i


print(f"* * * A soma é {s} * * *")
