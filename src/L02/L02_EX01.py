"""Resolução Lista 02 Exercicio 01 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios

# Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Digite valor n1...: '))
n2 = int(input('Digite valor n2...: '))

maior = 0

if n1 > n2:
    maior = n1
else:
    maior = n2

print(f'\n O maior valor é {maior}')
