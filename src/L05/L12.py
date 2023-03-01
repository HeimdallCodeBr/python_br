# -*- coding: utf-8 -*-

from os import system
from random import randint

"""Resolução Lista 05 Exercicio 12 Python Brasil (J.Siqueira 02/23)."""

"""
12. Embaralha palavra.

Construa uma função que receba uma string como parâmetro e devolva outra
string com os carateres embaralhados.

Por exemplo: se função receber a palavra python,  pode  retornar npthyo,
ophtyn  ou qualquer outra combinação possível, de forma aleatória.

Padronize em sua função que todos os caracteres serão devolvidos em
caixa alta ou caixa baixa, independentemente de como foram digitados.

"""
system('clear')


def embaralha_palavras(texto: str) -> tuple:
    t = len(texto)
    i = 0
    m: list = []
    texto_aleatoria = ''
    while True:
        a = randint(0, t-1)
        if len(m) >= t:
            break
        else:
            if a not in m:
                m.append(a)
                i += 1
            else:
                i -= 1
    for p in m:
        texto_aleatoria += texto[p]
    return texto_aleatoria.upper(), m


# ==================
# PROGRAMA PRINCIPAL
# ==================


print(embaralha_palavras('Tatuí Cidade de São Paulo'))
print(embaralha_palavras('Jefersom'))
