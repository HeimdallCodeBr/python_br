# -*- coding: utf-8 -*-

"""Resolução Lista 05 Exercicio 09 Python Brasil (J.Siqueira 02/23)."""

"""
9. Reverso do número.
Faça uma função que retorne o reverso de um número inteiro informado.

Por exemplo: 127 -> 721.

"""


def numero_reverso(n):
    return n[::-1]


print(numero_reverso('127'))
