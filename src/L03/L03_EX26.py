# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 26 Python Brasil (J.Siqueira 03/21)."""

# Numa eleição existem três candidatos. Faça um programa que peça o 
# número total de eleitores. Peça para cada eleitor votar e ao final
# mostrar o número de votos de cada candidato.

import os

os.system('clear')

p = int(input('Informe o numero de eleitores: '))
print('\n')
candidato_A = 0
candidato_B = 0
candidato_C = 0

for i in range(p):
    votacao = input(f'Eleitor: {i+1}, digite seu voto candidato A, B, C: ')
    if votacao.lower() == 'a':
        candidato_A += 1
    if votacao.lower() == 'b':
        candidato_B += 1
    if votacao.lower() == 'c':
        candidato_C += 1
print('='*50)
print(f'Candidato A: {candidato_A} voto(s)')
print(f'Candidato B: {candidato_B} voto(s)')
print(f'Candidato C: {candidato_C} voto(s)')
print('='*50)
