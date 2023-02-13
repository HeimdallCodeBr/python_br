# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 26 Python Brasil (J.Siqueira 03/21)."""

# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#
# a. Álcool:
# b. até 20 litros, desconto de 3% por litro
# c. acima de 20 litros, desconto de 5% por litro
#
# d. Gasolina:
# e. até 20 litros, desconto de 4% por litro
# f. acima de 20 litros, desconto de 6% por litro
#
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de
# combustível (codificado da # seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
# litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


litros = float(input('Informe quantos litros de combustivel foi colocado: '))
tipo = input('Informe o tipo de combustivel A-álcool, G-gasolina: ')

precoG = 2.5
precoA = 1.9
valor = 0
desconto = 0

if tipo in 'gG':
    if litros <= 20:
        valor = precoG * litros
        desconto = (precoG * litros) * 0.03
    else:
        valor = precoG * litros
        desconto = (precoG * litros) * 0.05
elif tipo in 'aA':
    if litros <= 20:
        valor = precoA * litros
        desconto = (precoA * litros) * 0.04
    else:
        valor = precoA * litros
        desconto = (precoA * litros) * 0.06
else:
    print('\n\033[1;31mValor inválido!\033[1;m')

print('\n* * * Cupom Fiscal * * *')
print(f'Valor total\t{valor}')
print(f'Desconto\t{desconto}')
print(f'Valor a pagar\t{valor - desconto}')
