# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 10 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Informe o 1º numero: "))
n2 = int(input("Informe o 2º numero: "))

for i in range(n1, n2 + 1):
    print(i)
