# -*- coding: utf-8 -*-
from random import randint

"""Resolução Lista 05 Exercicio 09 Python Brasil (J.Siqueira 02/23)."""

"""
9. Reverso do número.
Faça uma função que retorne o reverso de um número inteiro informado.

Por exemplo: 127 -> 721.

"""


def numero_reverso(n: str) -> str:
    '''
    numero_reverso:
                Função para inverter uma sequencia
    Parametros:
                n(str): sequencia numerica
    Retorna:
                (str): retorna o inverso da sequencia numerica
    '''
    return str(n)[::-1]


for i in range(10):
    a = str(randint(100, 999))
    print(f'{a} <=> {numero_reverso(a)}')
