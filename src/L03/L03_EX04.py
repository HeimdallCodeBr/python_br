# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 4 Python Brasil (J.Siqueira 03/21)."""

# Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma
# taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes
# com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
# número de anos necessários para que a população do país A ultrapasse ou iguale
# a população do país B, mantidas as taxas de crescimento.


populacao_A = 80000
populacao_B = 200000
i = 0
n = "-"
print("\n")

while True:
    populacao_A += populacao_A * (3 / 100)
    populacao_B += populacao_B * (1.5 / 100)
    i += 1

    print(f"Ano:{i:>3} | População A: {populacao_A:.7} | População B: {populacao_B:.7}")
    print(n * 55)

    if populacao_A >= populacao_B:
        print("\n")
        break
