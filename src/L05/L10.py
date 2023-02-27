# -*- coding: utf-8 -*-

from os import system
from random import randint

"""Resolução Lista 05 Exercicio 10 Python Brasil (J.Siqueira 02/23)."""

"""
10. Jogo de Craps.

Faça um programa de implemente um jogo de Craps.

O jogador lança um par de dados, obtendo um valor entre 2 e 12.

Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.

Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e
você perdeu.

Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".

Seu objetivo agora é continuar jogando os dados até tirar este número
novamente.

Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

"""


def jogarDados():
    return randint(1, 6)


def validaRegrasCraps(d1: int, d2: int, jogada: bool, p: int) -> int:
    resultado = d1 + d2
    r = 1
    if resultado in (7, 11) and jogada:
        r = 0  # Ganhou
    elif resultado in (2, 3, 12) and jogada or resultado == 7 and not jogada:
        r = -1  # Craps - Perdeu
    elif resultado in (4, 5, 6, 8, 9, 10) and jogada:
        r = resultado  # Ponto do Jogo
    elif resultado == p:
        r = 0
    else:
        r = 1  # Continua jogando
    return r


# ==================
# PROGRAMA PRINCIPAL
# ==================

lancamentos = 1
dado1 = 0
dado2 = 0
msn = 0
ponto = 0
lance = True
while True:
    system('clear')
    print(f'Lançamento nº {lancamentos} - Ponto do Jogo: {ponto}\n')
    jogar = input('Lançar dados [S]im ou [N]ão? ')
    if jogar.upper() == 'S':
        dado1 = jogarDados()
        dado2 = jogarDados()
        if lancamentos > 1:
            lance = False
        lancamentos += 1
        msn = (validaRegrasCraps(dado1, dado2, lance, ponto))
        print('------------------')
        print(f'Dado 1: [{dado1}]')
        print(f'Dado 2: [{dado2}]')
        print('------------------')
        print(f'Soma:   [{dado1+dado2}]\n')

        if msn == 0:
            print('> > > VENCEDOR! < < <')
            break
        elif msn == -1:
            print('PERDEU!')
            break
        elif msn > 1:
            ponto = msn
    else:
        break
    input('\nPressione qualquer tecla para continuar...')
