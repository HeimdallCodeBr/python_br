# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 35 Python Brasil (J.Siqueira 03/21)."""

# Encontrar números primos é uma tarefa difícil. Faça um programa que
# gera uma lista dos números primos existentes entre 1 e um número
# inteiro informado pelo usuário.

import os

os.system('clear')

n = int(input('\nDigite um numero: '))

for i in range(n+1):
    k = 0 
    if str(i) in '01':
        continue
    for j in range(2,i+1):
        if i%j == 0:
            k +=1
    if k == 1:
        print(f'\033[1;32m{i}\033[1;m')
