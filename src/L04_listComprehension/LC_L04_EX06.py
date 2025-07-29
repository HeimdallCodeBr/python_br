# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 06 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que peça as quatro notas de 10 alunos, calcule
# e armazene num vetor a média de cada aluno, imprima o número de
# alunos com média maior ou igual a 7.0.

from os import system
system('clear')



matriz = [[input(f'numero {j}: ') for j in range(i, i+3)] for i in range(1,8,3)]


print(matriz)
