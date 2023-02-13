# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 34 Python Brasil (J.Siqueira 03/21)."""

# Os números primos possuem várias aplicações dentro da Computação,
# por exemplo na Criptografia. Um número primo é aquele que é divisível
# apenas por um e por ele mesmo. Faça um programa que peça um número
# inteiro e determine se ele é ou não um número primo.

import os
os.system('clear')


n = int(input('\nDigite um numero: '))
k = 0

if str(n) in '01':
    print(f'\033[1;31m{n} não é primo\033[1;m\n')
else:
    for i in range(2,n):
        if n%i == 0:
            k +=1
    if k == 0:
        print(f'\033[1;32m{n} é primo\033[1;m\n')
    else:
        print(f'\033[1;31m{n} não é primo\033[1;m\n')