# -*- coding: utf-8 -*-

"""Resolução Lista 05 Exercicio 03 Python Brasil (J.Siqueira 02/23)."""

"""
3. Faça um programa, com uma função que necessite de três argumentos,

e que forneça a soma desses três argumentos.

"""


def soma_numeros(n1: int, n2: int, n3: int) -> int:
    '''
    SomaImposto:
                função soma 3 numero inteiros

    Parametros:
                n1 (int): numero do 1º argumento
                n2 (int): numero do 2º argumento
                n3 (int): numero do 3º argumento
    Retorna:
                Soma (int): retorna a soma dos 3 termos

    '''
    return n1+n2+n3


print(soma_numeros(2, 3, 5))
