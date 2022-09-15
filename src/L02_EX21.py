# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 21 Python Brasil (J.Siqueira 03/21)."""

# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
# usuário a valor do saque e depois informar quantas notas de cada valor serão
# fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O
# valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se
# preocupar com a quantidade de notas existentes na máquina.

# a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
#    notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

# b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três
#    notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro
#    notas de 1.


s = int(input('Informe o valor do saque: '))

t100 = s // 100
t50 = (s - (t100 * 100))//50
t10 = (s - ((t100 * 100) + (t50 * 50)))//10
t5 = (s - ((t100 * 100) + (t50 * 50) + (t10 * 10)))//5
t1 = (s - ((t100 * 100) + (t50 * 50) + (t10 * 10) + (t5 * 5)))

p = 's'

if s >= 10 and s <= 600:
    if t100 >= 1:
        print(f'{t100} nota de 100;')
    if t50 >= 1:
        print(f'{t50} nota de 50;')
    if t10 >= 1:
        print(f'{t10} nota de 10;')
    if t5 >= 1:
        print(f'{t5} nota de 5;')
    if t1 >= 1:
        print(f'{t1} moeda de 1;')
else:
    print('\n\033[1;31mValor inválido - saque permitido 10 a 600\033[1;m')
