# -*- coding: utf-8 -*-

"""Resolução Lista 05 Exercicio 08 Python Brasil (J.Siqueira 02/23)."""

"""
8. Faça uma função que informe a quantidade de dígitos de um determinado
número inteiro informado.

"""


def quantidade_digitos(n):
    return len(str(n))


# ==================
# PROGRAMA PRINCIPAL
# ==================
print(quantidade_digitos(23222447888))
