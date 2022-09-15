# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 39 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que leia dez conjuntos de dois valores, o primeiro
# representando o número do aluno e o segundo representando a sua 
# altura em centímetros. Encontre o aluno mais alto e o mais baixo.
# Mostre o número do aluno mais alto e o número do aluno mais baixo,
# junto com suas alturas.

import os

os.system('clear')

aluno =  []
altura = []

altura_menor = 1000
altura_maior = 0
soma =0
aluno =  ['c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16', 'c17', 'c19', 'c20']
altura = [199, 153, 200, 187, 207, 195, 193, 155, 180, 192]

for i in range (len(altura)):

    if altura[i] < altura_menor:
        altura_menor = altura[i]

    if altura[i] > altura_maior:
        altura_maior = altura[i]
        
    print(f'Aluno: {aluno[i]}\tAltura: {altura[i]}cm')
    print('-'*30)


print('\n')
print(f'Código aluno: {aluno[altura.index(altura_menor)]}')
print(f'Altura menor: {altura_menor}')
print('-'*30)
print(f'Código aluno: {aluno[altura.index(altura_maior)]}')
print(f'Altura maior: {altura_maior}')


