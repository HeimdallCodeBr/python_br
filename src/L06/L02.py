# -*- coding: utf-8 -*-

from os import system

"""Resolução Lista 06 Exercicio 02 Python Brasil (J.Siqueira 02/23)."""

"""
Nome ao contrário em maiúsculas.

Faça um programa que permita ao usuário digitar o seu nome
e em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. 

Dica: lembre-se que ao informar o nome o usuário pode
digitar letras maiúsculas ou minúsculas.

"""
system('clear')

nome = input('Digite um nome: ')

nome = nome.upper()

nome = nome[::-1]

print(nome)
