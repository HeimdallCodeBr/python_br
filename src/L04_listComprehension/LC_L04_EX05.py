# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 05 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

from os import system
system('clear')


vetor = [int(input(f'Digite um numero {i}: ')) for i in range(5)]

vetor_par = [par for par in vetor if par%2 == 0]
vetor_impar = [impar for impar in vetor if impar%2 != 0]

print (f'\nVetor principal: {vetor}')
print (f'Vetor com numeros pares {vetor_par}')
print (f'Vetor com numeros impares {vetor_impar}')





