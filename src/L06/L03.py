# -*- coding: utf-8 -*-

"""Resolução Lista 06 Exercicio 03 Python Brasil (J.Siqueira 02/23)."""

"""
Nome na vertical.

Faça um programa que solicite o nome do usuário
e imprima-o na vertical.

F
U
L
A
N
O

"""

nome = input('Digite um nome: ')

nome = nome.upper()

for i in nome:
    print(i)
