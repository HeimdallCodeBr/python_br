# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 08 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor. Imprima
# a idade e a altura na ordem inversa a ordem lida.

from os import system

idade = []
altura = []
i = 0
a = 0
c = 55

for k in range(5):
    k = (f'\033[1;33m{k+1}\033[1;m')
    system('clear')
    print('='*c)
    print(f'Informe os dados pessoa {k}')
    print('='*c)
    i = int(input(f'Informe a idade......: '))
    a = float(input(f'Informe a altura.....: '))
    print('-'*c)

    idade.append(i)
    altura.append(a)

system('clear')
print(f'Idade com vetor original.: {idade}')
print(f'Idade com vetor inverso..: {idade[::-1]}')
print('-'*c)
print(f'Altura com vetor original: {altura}')
print(f'Altura com vetor inverso.: {altura[::-1]}')
