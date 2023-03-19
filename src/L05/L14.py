# -*- coding: utf-8 -*-
from os import system
from random import randint

system('clear')

"""Resolução Lista 05 Exercicio 14 Python Brasil (J.Siqueira 02/23)."""

"""
14. Quadrado mágico.

Um quadrado mágico é aquele dividido em linhas e colunas, com um número
em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma.

Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos
com as características acima.

Dica: produza todas as combi nações possíveis e verifique a soma quando
completar cada quadrado.  Usar um vetor de 1 a 9 parece ser mais simples que
usar uma matriz 3x3.
"""
# =======================================
# Valida se a matriz é um quadrado mágico
# =======================================


def quadrado_magico(matriz: list) -> tuple:
    resultado_linha: list = []
    resultado_coluna: list = []
    li: int = 0
    co: int = 0
    de: int = 0
    dd: int = 0
    for i, linha in enumerate(matriz):  # linha
        li += sum(linha)
        resultado_linha.append(li)
        li = 0
        for j, coluna in enumerate(matriz):  # coluna
            co += matriz[j][i]
        resultado_coluna.append(co)
        co = 0
        print(j, i, matriz[j][i])

    verificado = True
    for vli in resultado_linha:
        for vco in resultado_coluna:
            if vli != vco:
                verificado = False
    return verificado, resultado_coluna, resultado_linha

    # =======================================
    # Gera matriz aleatoria
    # =======================================


def gera_matriz(tamanho: int) -> list:
    matriz: list = []
    aux: list = []

    for j in range(tamanho):
        for i in range(tamanho):
            a = randint(1, 9)
            aux.append(a)
        matriz.append(aux)
        aux = []
    return matriz


# ==================
# PROGRAMA PRINCIPAL
# ==================


mk = [
    [8, 3, 9],
    [1, 4, 9],
    [6, 7, 4]
]

mj = [
    [4, 7, 7, 1, 5],
    [9, 3, 5, 8, 6],
    [4, 6, 5, 2, 8],
    [4, 2, 5, 1, 3],
    [2, 9, 5, 8, 1]
]


m = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2],
]


k = 0
while True:
    system('clear')
    r = randint(3, 3)
    g = m  # gera_matriz(r)
    v = quadrado_magico(g)
    resultado, coluna, linha = v
    print('\n----------------------------')
    print(f'Matriz: {resultado} => {g}')
    print(f'Numero de interações {k} ')
    print(f'Coluna: {coluna}')
    print(f'Linha:  {linha}')
    print('----------------------------\n')
    if resultado:
        break
    else:
        k += 1


# ----------------------------
# Matriz: True =>
# [
# [4, 2, 7],
# [8, 3, 2],
# [1, 8, 4]
# ]
# Numero de interações 74
# Coluna: [13, 13, 13]
# Linha:  [13, 13, 13]
# ----------------------------

dd
