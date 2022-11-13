# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 22 Python Brasil (J.Siqueira 03/21)."""

# Faça um Programa que peça um número inteiro e determine se ele é
# par ou impar. Dica: utilize o operador módulo (resto da divisão).

n = int(input ('Digite um numero: '))

if n % 2 == 0:
    print(f'\n{n} é numero par')
else:
    print(f'\n{n} é numero impar')
