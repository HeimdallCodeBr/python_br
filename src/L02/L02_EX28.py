# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 28 Python Brasil (J.Siqueira 03/21)."""

# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
# Confira:
#               Até 5 Kg            Acima de 5 Kg
# File Duplo    R$ 4,90 por Kg      R$ 5,80 por Kg
# Alcatra       R$ 5,90 por Kg      R$ 6,80 por Kg
# Picanha       R$ 6,90 por Kg      R$ 7,80 por Kg
#
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos
# tipos de carne da promoção, porém não há limites para a quantidade de carne
# por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda
# um desconto de 5% sobre o total da compra. Escreva um programa que peça o
# tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total,
# tipo de pagamento, valor do desconto e valor a pagar.


quantidade = float(input("Informe quantos [kg] de carne...............: "))
tipo_produto = input("Qual tipo [F]ile, [A]lcatra, [P]icanha......: ")
tipo_pagamento = input("Qual forma de pagamento [D]inheiro, [C]artão: ")

desconto = 0
valor = 0

if tipo_produto in "fF":
    tipo_produto = "File duplo"
    if quantidade <= 5:
        valor = 5.9 * quantidade
    else:
        valor = 6.8 * quantidade
elif tipo_produto in "aA":
    tipo_produto = "Alcatra"
    if quantidade <= 5:
        valor = 4.9 * quantidade
    else:
        valor = 5.8 * quantidade
elif tipo_produto in "pP":
    tipo_produto = "Picanha"
    if quantidade <= 5:
        valor = 6.9 * quantidade
    else:
        valor = 7.8 * quantidade
else:
    print("\n\033[1;31mValor inválido!\033[1;m")

if tipo_pagamento in "cC":
    tipo_pagamento = "Cartão"
    desconto = 0.05 * valor
else:
    tipo_pagamento = "Dinheiro"
    desconto = 0

if quantidade >= 0:
    print("\n* * * Cupom Fiscal * * *\n")
    print(f"{tipo_produto}\t\t\t{quantidade:.1f}kg")
    print("-----------------------------------------")
    print(f"Valor total\t\t\t{valor:.2f}")
    print(f"Forma de pagamento\t\t{tipo_pagamento}")
    print(f"Desconto 5%\t\t\t{desconto:.2f}")
    print(f"Valor a pagar\t\t\t{((valor) - desconto):.2f}\n")
