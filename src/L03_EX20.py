# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 20 Python Brasil (J.Siqueira 03/21)."""

# Altere o programa de cálculo do fatorial, permitindo ao usuário
# calcular o fatorial várias vezes e limitando o fatorial a números
# inteiros positivos e menores que 16.


while True:
    f = 1
    i = 2
    c = 0
    n = int(input(f'{c}.Informe um numero para caucular fatorial [n!]: '))
    c += 1
    if n > 16:
        print ('\033[1;31mErro! digite numeros menores que 16\033[1;m\n')
        break
    else:
        for i in range(2, n+1):
            f = f * i
        print(f'\033[1;32mFatorial [{n}!]: {f}\033[1;m\n')
