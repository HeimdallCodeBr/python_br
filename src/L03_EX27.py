# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 27 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para
# cada turma. As turmas não podem ter mais de 40 alunos.


import os

os.system('clear')

t = int(input('Informe a quantidade de turmas: '))
print('='*50)
i = 0
m = 0

while i < t:
    a = int(input(f'Informe a quantidade de alunos na turma {i+1}: '))
    if a <= 40:
        m = m + a
        pass
    else:
        print ('\033[1;31mErro!\033[1;m')
        i -= 1
    i +=1

print('='*50)
print(f'Média é {m/t:.0f} alunos por turma')
print('='*50)



