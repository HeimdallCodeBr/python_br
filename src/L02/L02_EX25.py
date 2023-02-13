# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 25 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"
#
# O programa deve no final emitir uma classificação sobre a participação da
# pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
# ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
# "Assassino". Caso contrário, ele será classificado como "Inocente".

p1 = input('Telefonou para vítima?....: ')
p2 = input('Esteve no local do crime?.: ')
p3 = input('Mora perto da vítima?.....: ')
p4 = input('Devia para vítima?........: ')
p5 = input('Já trabalhou com a vítima?: ')

r = 0

if p1 in 'sS':
    r += 1
if p2 in 'sS':
    r += 1
if p3 in 'sS':
    r += 1
if p4 in 'sS':
    r += 1
if p5 in 'sS':
    r += 1

if r <= 2:
    print('\nSuspeita')
if r >= 3 and r <= 4:
    print('\nCúmplice')
if r >= 5:
    print('\nAssassino')
