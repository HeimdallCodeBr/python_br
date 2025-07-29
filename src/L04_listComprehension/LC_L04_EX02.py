# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 02 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.


import os

os.system('clear')

vetor = [int(input(f'Digite um numero {n}: ')) for n in range(3)]

print (f'\nVetor com ordem valores digitados: {vetor}')
print (f'Vetor com ordem valores inverso..: {vetor[::-1]}')