# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 24 Python Brasil (J.Siqueira 03/21)."""

# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
# operação ele deseja realizar. O resultado da operação deve ser acompanhado
# de uma frase que diga se o número é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.

n1 = int(input('Digite primeiro numero...........: '))
n2 = int(input('Digite segundo numero............: '))
op = input('Digite a operação [+] [-] [/] [*]: ')
r = 0
r1 = 'impar'
r2 = 'negativo'
r3 = 'decimal'

if op == '+':
    r = n1 + n2
elif op == '-':
    r = n1 - n2
elif op == '*':
    r = n1 * n2
elif op == '/':
    r = n1 / n2

if r % 2 == 0:
    r1 = 'par'
if r >= 0:
    r2 = 'positivo'
if round(r) % r == 0:
    r3 = 'inteiro'


print(f'\nResultado é \033[1;34m{r:.1f}\033[1;m,')
print(f'\033[1;36m{r1}\033[1;m')
print(f'\033[1;36m{r2}\033[1;m')
print(f'\033[1;36m{r3}\033[1;m')
