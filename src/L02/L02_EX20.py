# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 20 Python Brasil (J.Siqueira 03/21)."""

# Faça um Programa para leitura de três notas parciais de um aluno. O programa
# deve calcular a média alcançada por aluno e presentar:

#       a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a
#          respectiva média alcançada;

#       b. A mensagem "Reprovado", se a média for menor do que 7, com a
#          respectiva média alcançada;

#       c. A mensagem "Aprovado com Distinção", se a média for igual a 10.


n1 = float(input('Informe nota 1: '))
n2 = float(input('Informe nota 2: '))
n3 = float(input('Informe nota 3: '))

m = (n1+n2+n3)/3

if m < 7:
    print(f'\nMédia: {m:.1f}\tReprovado')
elif m >= 7 and m < 10:
    print(f'\nMédia: {m:.1f}\tAprovado')
elif m == 10:
    print(f'\nMédia: {m:.1f}\tAprovado com distinção')
