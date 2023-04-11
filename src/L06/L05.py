# -*- coding: utf-8 -*-

"""Resolução Lista 06 Exercicio 05 Python Brasil (J.Siqueira 02/23)."""

"""
Nome na vertical em escada invertida.

Altere o programa anterior de modo que
a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F

"""

nome = input('Digite um nome: ')

nome = nome.upper()

tamanho = len(nome)

print(nome)
for i in range(1, tamanho):
    print(nome[:-i])
