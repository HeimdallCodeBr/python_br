# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 07 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.


from os import system
from random import randint

system('clear')

c = 60
k = 0
vetor = []
soma = 0
produto = 1

while k < 5:

    n = str(randint(1, 100))

    if n.isnumeric():
        k += 1
        soma += int(n)
        produto = produto * int(n)
        vetor.append(n)
    else:
        print('\033[1;31mERRO! digite novamente...\033[1;m')

system('clear')
print('='*c)
print('SAIDA DO PROGRAMA')
print('='*c)
print(f'Valores digitados........: \033[1;32m{vetor}\033[1;m')
print('-'*c)
print(f'Soma dos valores.........: \033[1;32m{soma}\033[1;m')
print('-'*c)
print(f'Multiplicação dos valores: \033[1;32m{produto}\033[1;m')
print('-'*c)


# ============================================================
# SAIDA DO PROGRAMA
# ============================================================
# Valores digitados........: ['61', '11', '33', '52', '68']
# ------------------------------------------------------------
# Soma dos valores.........: 225
# ------------------------------------------------------------
# Multiplicação dos valores: 78297648
# ------------------------------------------------------------
