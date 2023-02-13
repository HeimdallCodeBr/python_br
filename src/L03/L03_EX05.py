# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 5 Python Brasil (J.Siqueira 03/21)."""

# Altere o programa anterior permitindo ao usuário informar as populações e
# as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

print("\n")
populacao_A = float(input("Informe a população A............................: "))
taxa_A = float(input("Infome a taxa de crescimento anual da população A: "))
populacao_B = float(input("Informe a população B............................: "))
taxa_B = float(input("Infome a taxa de crescimento anual da população B: "))


i = 0
n = "-"
print("\n")

while True:
    populacao_A += populacao_A * (taxa_A / 100)
    populacao_B += populacao_B * (taxa_B / 100)
    i += 1

    print(f"Ano:{i:>3} | População A: {populacao_A:.7} | População B: {populacao_B:.7}")
    print(n * 55)

    if populacao_A >= populacao_B:
        print("\n")
        break
