"""Resolução Lista 02 Exercicio 09 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios


# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = 2
n2 = 3
n3 = 1
t = 0

print(f'valor n1: {n1}')
print(f'valor n2: {n2}')
print(f'valor n3: {n3}')

if n2 > n1:
    t = n1
    n1 = n2
    n2 = t

if n3 > n2:
    t = n2
    n2 = n3
    n3 = t

if n2 > n1:
    t = n1
    n1 = n2
    n2 = t


print('===============')
print(f'valor n1: {n1}')
print(f'valor n2: {n2}')
print(f'valor n3: {n3}')
