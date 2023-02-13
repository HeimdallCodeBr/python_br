# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 09 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

from math import pow
from os import system

system('clear')

vetor = []
soma = 0
i = 0
c = 50

print('='*c)
print('SAIDA DO PROGRAMA')
print('='*c)
print('\n')


while i < 10:
    m = str(i+1).zfill(2)
    n = input(f'Informe um numero inteiro [{m}]: ')
    print('-'*c)

    if n.isnumeric() == True:
        j = pow(int(n), 2)
        soma += j
        vetor.append(f'{j:.0f}')
        i += 1
    else:
        print('\033[1;31mERRO! digite novamente...\033[1;m')


print(f'\nSoma dos quadrados..: {soma:.0f}')
print(f'\nVetor ao quadrado...: {vetor}\n')
