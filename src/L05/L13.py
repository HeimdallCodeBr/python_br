# -*- coding: utf-8 -*-
from os import system
from random import randint

"""Resolução Lista 05 Exercicio 13 Python Brasil (J.Siqueira 02/23)."""

"""
13. Desenha moldura.

Construa uma função que desenhe um retângulo usando os caracteres "+",
"-" e "| ".

Esta função deve receber dois parâmetros, linhas  e colunas, sendo que o
valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.

Se valores fora da faixa forem informados, eles devem ser modificados
para valores dentro da faixa de forma elegante.

"""


def desenha_moldura(tc: int, tl: int) -> str:
    if tc > 20 or tl > 20:
        return str(None)
    else:
        desenho = ''
        # SIMBOLOS
        ca = '+'
        sp = '  '
        # COLUNAS
        co = '--'
        coluna = ca + (co * tc) + ca
        # LINHAS
        li = '|'
        linha = ''
        for i in range(tl):
            linha += '\n' + li + (sp * tc) + li
        desenho = coluna + linha + '\n' + coluna
        return desenho


# ==================
# PROGRAMA PRINCIPAL
# ==================
while True:
    system('clear')
    for z in range(1):
        tc = randint(1, 25)
        tl = randint(1, 25)
        print(f'Tamanho Coluna {tc} x Linha {tl}')
        print(desenha_moldura(tc, tl))
    s = input('Digite 0 para sair')
    if s == '0':
        break
