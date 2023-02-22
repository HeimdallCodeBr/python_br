# -*- coding: utf-8 -*-

"""Resolução Lista 05 Exercicio 02 Python Brasil (J.Siqueira 02/23)."""

"""
2. Faça um programa para imprimir:
    1 
    1   2  
    1   2   3  
   . ....  
    1   2   3  . ..  n
para um n informado pelo usuário. 

Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def imprimi_numeros(n):
    r = ''
    for i in range(1, n+1):
        r += '\n'
        for k in range(1, i+1):
            r += (str(k) + ' ')
    return r + '\n'


print(imprimi_numeros(7))
