# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 03 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


import os

os.system('clear')

nota_media = [float(input(f'Digite a nota {n}: ')) for n in range(4)]
media = sum(nota_media)/len(nota_media)


print (f'\nMédia das notas é: {media} ')