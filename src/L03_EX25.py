# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 25 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que peça para n pessoas a sua idade, ao final o 
# programa devera verificar se a média de idade da turma varia entre 
# 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem,
# adulta ou idosa, conforme a média calculada.

# g1    jovem      0 - 25
# g2    adulto     26 - 60
# g3    idoso      >60


import os, time

os.system('clear')

inicio = time.time()

n = int(input('Informe o numero de pessoas: '))
s = 0
m = 0

for i in range(n):
    idade = int(input(f'Pessoa {i+1}: '))
    s += idade

m = s/n
if m > 0 and m < 25:
    print(f'Pela média de {m}, o grupo é Jovem')
if m > 26 and m < 60:
    print(f'Pela média de {m}, o grupo é Adulto')
if m >= 60:
    print(f'Pela média de {m}, o grupo é Idoso')
    
termino = time.time()
print(f'\n\033[1;44mTempo de Execução: {termino - inicio:.1f} segundos\033[1;m\n')



