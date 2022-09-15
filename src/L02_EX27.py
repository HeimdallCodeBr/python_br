# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 27 Python Brasil (J.Siqueira 03/21)."""

# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#           Até 5 Kg            Acima de 5 Kg
# Morango   R$ 2,50 por Kg      R$ 2,20 por Kg
# Maçã      R$ 1,80 por Kg      R$ 1,50 por Kg
#
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
# ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

f1 = float(input('Quantidade em [kg] de maça...: '))
f2 = float(input('Quantidade em [kg] de morango: '))

f1_preco = 0
f2_preco = 0
desconto = 0

if f1 <= 5:
    f1_preco = f1 * 2.5
else:
    f1_preco = f1 * 2.2

if f2 <= 5:
    f2_preco = f2 * 1.8
else:
    f2_preco = f2 * 1.5

if (f1 + f2) >= 8 or (f1_preco + f2_preco) >= 25:
    desconto = (f1_preco + f2_preco) * 0.01

print('\n* * * Cupom Fiscal * * *\n')
print(f'Morangos\t{f1}kg\t\t{f1_preco:.2f}')
print(f'Maças\t\t{f2}kg\t\t{f2_preco:.2f}')
print('-----------------------------------------')
print(f'Valor total\t\t\t{f1_preco + f2_preco:.2f}')
print(f'Desconto 10%\t\t\t {desconto:.2f}')
print(f'Valor a pagar\t\t\t{((f1_preco + f2_preco) - desconto):.2f}')
