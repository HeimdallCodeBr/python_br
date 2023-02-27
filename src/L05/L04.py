# -*- coding: utf-8 -*-

"""Resolução Lista 05 Exercicio 04 Python Brasil (J.Siqueira 02/23)."""

"""
4. Faça um programa, com uma função que necessite de um argumento.

A função retorna o valor de caractere "P", se seu argumento for positivo,

e "N", se seu argumento for zero ou negativo.

"""


def polaridade_numero(n: int) -> str:
    '''
    SomaImposto:
                função verifica se numero é positivo(+) ou negativo(-)

    Parametros:
                n (int): numero real

    Retorna:
                'P' (str): para numeros > 0
                'N' (str): para numeros <= 0

    '''
    if n < 1:
        return 'N'
    else:
        return 'P'


# ==================
# PROGRAMA PRINCIPAL
# ==================
print(polaridade_numero(6))
print(polaridade_numero(-4))
print(polaridade_numero(0))
