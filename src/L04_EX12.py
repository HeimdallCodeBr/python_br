# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 12 Python Brasil (J.Siqueira 04/22)."""

# Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais
# de 13 anos possuem altura inferior à média de altura
# desses alunos.

from os import system
from random import randint

system('clear')

idade = []
altura = []
alunos = 30
soma_altura = 0
media_altura = 0

for i in range(alunos):
    a = randint(8, 16)
    b = randint(70, 180)

    soma_altura += b
    idade.append(a)
    altura.append(b)

media_altura = (soma_altura/alunos)
print('IDADE     | ALTURA')
print('------------------')
for i in range(alunos):
    if idade[i] > 13 and media_altura > altura[i]:
        print(f'\033[1;32m◼\033[1;m {idade[i]} anos | {altura[i]} cm')
    # else:
    #     print (f'◻ {idade[i]} anos | {altura[i]} cm')

print('\n')
print(f'Média de altura: {media_altura:.0f}')
print('\n')
print('DADOS BRUTOS')
print('\n')
print(f'Idades: {idade}')
print(f'Altura: {altura}')
print('\n')

# IDADE     | ALTURA
# ------------------
# ◼ 16 anos | 110 cm
# ◼ 16 anos | 100 cm
# ◼ 18 anos | 100 cm
# ◼ 15 anos | 111 cm
# ◼ 17 anos | 102 cm
# ◼ 15 anos | 119 cm
# ◼ 15 anos | 110 cm
# ◼ 15 anos | 108 cm
# ◼ 18 anos | 134 cm
# ◼ 16 anos | 111 cm


# Média de altura: 136


# DADOS BRUTOS


# Idades: [18, 16, 13, 13, 15, 16, 12, 18, 15, 17, 12, 17, 14, 18, 15, 13, 12, 18, 15, 17, 15, 18, 13, 14, 13, 16, 12, 14, 12, 12]
# Altura: [158, 110, 137, 124, 161, 100, 165, 100, 111, 163, 158, 102, 171, 142, 119, 102, 175, 149, 110, 163, 108, 134, 138, 175, 166, 111, 126, 148, 103, 140]
