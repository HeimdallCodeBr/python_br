# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 8 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que leia 5 números e informe a soma e a média dos números.


i = 0
s = 0

while True:
    n = int(input(f"Informe {i+1}º numero: "))
    i += 1
    s += n

    if i == 5:
        break


print(f"A soma é {s} e a média é {s/i}")
