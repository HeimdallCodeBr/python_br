# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 04 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
# consoantes foram lidas. Imprima as consoantes.

from os import system
system('clear')


vetor = [input(f'Digite uma letra {c}: ') for c in range(10)]

consoantes = [char for char in vetor if char.isalpha() and char.lower() in "aeiou"]

print(f'\nForam digitadas um total de  {len(consoantes)} consoante(s)')