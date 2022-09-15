"""Resolução Lista 02 Exercicio 07 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios


# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Digite valor n1: '))
n2 = int(input('Digite valor n2: '))
n3 = int(input('Digite valor n3: '))

maior = n1
menor = n1

if n1 > n2:
    maior = n1
else:
    maior = n2
    if n3 > maior:
        maior = n3


if n1 < n2:
    menor = n1
else:
    menor = n2
    if n3 < menor:
        menor = n3


print(f'\nValor maior {maior}')
print(f'\nValor menor {menor}')
