# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 36 Python Brasil (J.Siqueira 03/21)."""

# Desenvolva um programa que faça a tabuada de um número qualquer inteiro
# que será digitado pelo usuário, mas a tabuada não deve necessariamente
# iniciar em 1 e terminar em 10, o valor inicial e final devem ser
# informados também pelo usuário, conforme exemplo abaixo:

# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35

# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

import os 

while True:

    os.system('clear')

    t = int(input("Informe a tabuada a ser gerada: "))
    a = int(input('Informe o inicio da tabuada: '))
    b = int(input('Informe o termino da tabuada: '))

    print(f"\n* * * * * TABUADA DO {t} * * * * *")

    if b < a:
        print('Erro! o numero final não pode ser menor que numero inicial')
    else:
        for i in range(a, b+1):
            print(f'{t} x {i} = {t * i}')
    
    continua = input('\nDeseja continuar [S/n]: ')
    if continua in 'Nn':
        break


