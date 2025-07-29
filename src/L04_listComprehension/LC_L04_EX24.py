# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 24 Python Brasil (J.Siqueira 04/22)."""

# Faça um programa que simule um lançamento de dados. Lance o dado 100
# vezes e armazene os resultados em um vetor.  Depois, mostre quantas
# vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6)
# e uma função para gerar numeros aleatórios, simulando os lançamentos dos
# dados.

from os import system
from random import randint

system('clear')

dado = [1, 2, 3, 4, 5, 6]
jogadas = [0] * 6

for i in range(100):
    a = randint(1, 6)
    if a in dado:
        jogadas[dado.index(a)] += 1
print('Face Jogadas')
for m in range(len(dado)):
    print(f'{str(m+1).ljust(5)}{str(jogadas[m]).ljust(5)}')
print(f'Total jogadas {sum(jogadas)}')
