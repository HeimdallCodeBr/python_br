# -*- coding: utf-8 -*-

"""Resolução Lista 05 Exercicio 01 Python Brasil (J.Siqueira 02/23)."""

"""
1. Faça um programa para imprimir:
    1
    2   2
    3   3   3
   . .... 
    n   n   n   n   n   n . .. n

para um n informado pelo usuário. Use uma função que receba um valor 
n inteiro e imprima até a n-ésima linha.
"""


def imprimi_numeros(n):
    r = ''
    for i in range(1, int(n)+1):
        r = r + ('{}\n').format((str(i)+'  ') * i)
    return r


print(imprimi_numeros(5))
