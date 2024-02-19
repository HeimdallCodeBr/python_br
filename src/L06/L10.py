# -*- coding: utf-8 -*-

"""Resolução Lista 06 Exercicio 10 Python Brasil (J.Siqueira 02/23)."""

"""
Número por extenso.

Escreva um programa que solicite ao usuário
a digitação de um número até 99 e imprima-o
na tela por extenso.
"""


def numero_extenso(numero: int) 
    valor = ''
    unidade = {
        0: 'zero',
        1: 'um',
        2: 'dois',
        3: 'três',
        4: 'quatro',
        5: 'cinco',
        6: 'seis',
        7: 'sete',
        8: 'oito',
        9: 'nove',
    }

    dezena = {
        10: 'dez',
        11: 'onze',
        12: 'doze',
        13: 'treze',
        14: 'quatorze',
        15: 'quinze',
        16: 'dezesseis',
        17: 'dezessete',
        18: 'dezoito',
        19: 'dezenove',
        20: 'vinte',
        30: 'trinta',
        40: 'quarenta',
        50: 'cinquenta',
        60: 'sessenta',
        70: 'setenta',
        80: 'oitenta',
        90: 'noventa'
    }

    if numero <= 9:
        valor = str(unidade[numero])
    elif numero > 9 and numero <= 19:
        valor = str(dezena[numero])
    elif numero > 19 and numero <= 99:
        chave_u = int(str(numero)[1])
        chave_d = numero - chave_u
        if chave_u == 0:
            valor = dezena[chave_d]
        else:
            valor = (f'{dezena[chave_d]} e {unidade[chave_u]}')
    else:
        valor = 'ERRO'

    return valor


# ==================
# PROGRAMA PRINCIPAL
# ==================
print('\n')
numero = int(input('Digite um numero entre 0 e 99: '))
print(numero, ' - ', numero_extenso(numero))
