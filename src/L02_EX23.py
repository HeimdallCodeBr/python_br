# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 23 Python Brasil (J.Siqueira 03/21)."""

# Faça um Programa que peça um número e informe se o número é inteiro
# ou decimal. Dica: utilize uma função de arredondamento.

n = float(input('Digite um numero: '))

if round(n) % n == 0:
    print('\nnumero inteiro')
else:
    print('\nnumero decimal')
