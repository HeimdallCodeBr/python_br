"""Resolução Lista 02 Exercicio 08 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios


# Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


p1 = int(input('Digite valor produto 1: '))
p2 = int(input('Digite valor produto 2: '))
p3 = int(input('Digite valor produto 3: '))

menor = 0

if p1 < p2:
    menor = p1
else:
    menor = p2
    if p3 < menor:
        menor = p3


print(f'O produto com menor valor é {menor:.2f}R$\n')
