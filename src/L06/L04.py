# -*- coding: utf-8 -*-

"""Resolução Lista 06 Exercicio 04 Python Brasil (J.Siqueira 02/23)."""

"""
Nome na vertical em escada.

Modifique o programa anterior de forma a 
mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO

"""

nome = input('Digite um nome: ')

nome = nome.upper()

escala = ''

for i in nome:
    escala += i
    print(escala)
