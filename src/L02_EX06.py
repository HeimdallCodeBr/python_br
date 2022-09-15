"""Resolução Lista 02 Exercicio 06 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios


# Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('Digite valor n1: '))
n2 = int(input('Digite valor n2: '))
n3 = int(input('Digite valor n3: '))

maior = 0

if n1 > n2:
    maior = n1
else:
    maior = n2
    if n3 > maior:
        maior = n3


print(f'\nO maior valor é {maior}')
