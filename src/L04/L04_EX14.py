# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 14 Python Brasil (J.Siqueira 04/22)."""

# Utilizando listas faça um programa que faça 5 perguntas para uma
# pessoa sobre um crime. As perguntas são:

# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"
#
# O programa deve no final emitir uma classificação sobre a participação
# da pessoa no crime.
#
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#
# Caso contrário, ele será classificado como "Inocente".


from os import system

system('clear')

soma = 0
c = 50

perguntas = ['a. Telefonou para a vítima?  ',
             'b. Esteve no local do crime? ',
             'c. Mora perto da vítima?     ',
             'd. Devia para a vítima?      ',
             'e. Já trabalhou com a vítima?']

print("=" * c)
print("RESPONSA COM 'S' PARA SIM E 'N' PARA NÃO")
print("=" * c)

for i in perguntas:
    resposta = input(f'{i}: ')
    if resposta.lower() == 's':
        soma += 1

if soma <= 1:
    print('inocente')
elif soma > 1 and soma <= 2:
    print('suspeita')
elif soma >= 3 and soma <= 4:
    print('cúmplice')
else:
    print('assassino')
