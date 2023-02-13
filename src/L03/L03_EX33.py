# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 33 Python Brasil (J.Siqueira 03/21)."""

# O Departamento Estadual de Meteorologia lhe contratou para desenvolver
# um programa que leia as um conjunto indeterminado de temperaturas, 
# informe ao final a menor e a maior temperaturas informadas, bem como 
# a média das temperaturas.

import random, os

os.system('clear')

temperatura = []
maior = 0
menor = 100
soma = 0

for i in range(10):
    x = random.randint(0, 80)
    soma += x
    temperatura.append(x)

    if x < menor:
        menor = x
    if x > maior:
        maior = x

media = soma/len(temperatura)
print(f'\nTemperaturas em ॰C: {temperatura}\n')
print(f'Valor menor: {menor:.1f} ॰C')
print(f'Valor maior: {maior:.1f} ॰C')
print(f'Valor médio: {media:.1f} ॰C')
print('\n')


