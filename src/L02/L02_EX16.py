# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 16 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios

# Faça um programa que calcule as raízes de uma equação do segundo grau, na
# forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer
# as consistências, informando ao usuário nas seguintes situações:

#   a. Se o usuário informar o valor de A igual a zero, a equação não é do
#      segundo grau e o programa não deve fazer pedir os demais valores,
#      sendo encerrado;

#   b. Se o delta calculado for negativo, a equação não possui raizes reais.
#      Informe ao usuário e encerre o programa;

#   c. Se o delta calculado for igual a zero a equação possui apenas uma raiz
#       real; informe-a ao usuário;

#   d. Se o delta for positivo, a equação possui duas raiz reais; informe-as
#      ao usuário;

# a = 1, b = 4, c = 5 (delta < 0, não é equação do segundo grau)
# a = 4, b = 4, c = 1 (delta = 0, possui somente uma raiz)
# a = 1, b = 5, c = 6 (delta > 0, possui duas raizes)


from math import sqrt

a = float(input('Informe o valor de a: '))

if a == 0:
    print('\nValor de a = 0, não é equação do segundo grau!')
else:
    b = float(input('Informe o valor de b: '))
    c = float(input('Informe o valor de c: '))
    delta = (pow(b, 2)) - 4 * a * c
    if delta < 0:
        print(f'\nValor do delta {delta} é negativo, não possui raizes')
    else:
        if delta == 0:
            print(f'\nValor do delta {delta} - uma raiz')
            print(f'\nRaiz de x = {(-b)/(2*a)}')
        else:
            print(f'\nValor do delta {delta} - duas raiz')
            print(f"\nRaiz de x' = {(-b)+(sqrt(delta))/2*a}")
            print(f"\nRaiz de x\" = {(-b)-(sqrt(delta))/2*a}")
