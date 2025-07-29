# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 13 Python Brasil (J.Siqueira 04/22)."""

# Faça um programa que receba a temperatura média de cada mês do ano
# e armazene-as em uma lista. Após isto, calcule a média anual das
# temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

import os
import random

os.system('clear')

mes = ['Janeiro',
       'Fevereiro',
       'Março',
       'Abril',
       'Maio',
       'Junho',
       'Julho',
       'Agosto',
       'Setembro',
       'Outubro',
       'Novembro',
       'Dezembro']

temperatura_media = []


for t in mes:
    temperatura_media.append(random.randint(0, 45))

temperatura_media_anual = (sum(temperatura_media))/(len(mes))
print('Temperatura Média Anual: {:.1f}'.format(temperatura_media_anual))
print('-'*40)

for i, k in enumerate(mes):
    if temperatura_media[i] > temperatura_media_anual:
        print('{} - {}︒C'.format(k, temperatura_media[i]))
