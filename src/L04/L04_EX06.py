# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 06 Python Brasil (J.Siqueira 04/22)."""

# Faça um Programa que peça as quatro notas de 10 alunos, calcule
# e armazene num vetor a média de cada aluno, imprima o número de
# alunos com média maior ou igual a 7.0.

from os import system

lancamento = []
nota = []
aluno = []
soma = 0
media = []
k = 0
c = 40

while k < 3:

    system('clear')
    print('='*c)
    print('LANÇAMENTO DE NOTAS PROVAS')
    print('='*c)

    nome = input(f'Informe o nome do aluno [{k+1}]: ')
    if nome == '':
        break
    aluno.append(nome)
    k += 1

    for i in range(4):
        print('-'*c)
        a = int(input(f'Informe a nota [{i+1}]: '))
        nota.append(a)
        soma += a

    lancamento.append(nota)
    media.append(soma/4)
    nota = []
    soma = 0

system('clear')
print('='*c)
print('RELAÇÃO DE ALUNOS APROVADOS')
print('='*c)

for i in range(k):
    if media[i] >= 7:
        print(
            f'{aluno[i]} - {media[i]:.1f}: \033[1;32mpassou\033[1;m')
    else:
        print(f'{aluno[i]} - {media[i]:.1f}: \033[1;31mnão passou\033[1;m')
    print('-'*c)

print('\n')
