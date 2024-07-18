# -*- coding: utf-8 -*-

import os

"""Resolução Lista 06 Exercicio 01 Python Brasil (J.Siqueira 02/23)."""

"""
Tamanho de strings.

Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.

Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings

String 1: Brasil Hexa 2006 
String 2: Brasil! Hexa 2006!

Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres

As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.

"""
os.system('clear')


s1 = 'Brasil Hexa 2006?'
s2 = 'Brasil Hexa 2006?'


print(f'Tamanho de "{s1}": {len(s1)} caracteres')
print(f'Tamanho de "{s2}": {len(s2)} caracteres')
print('\n')

if s1 == s2:
    print('As duas strings possuem conteúdo iguais.')
else:
    print('As duas strings possuem conteúdo diferente.')


if len(s1) == len(s2):
    print('As duas strings possuem conteúdo iguais.')
else:
    print('As duas strings possuem conteúdo diferente.')
