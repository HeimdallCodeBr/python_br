"""Resolução Lista 02 Exercicio 13 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios

# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor
# inválido.

s = int(input('Digite um numero de 1 a 7 da semana: '))

if s == 1:
    print('Domingo')
elif s == 2:
    print('Segunda-feira')
elif s == 3:
    print('Terça-feira')
elif s == 4:
    print('Quarta-feira')
elif s == 5:
    print('Quinta-feira')
elif s == 6:
    print('Sexta-feira')
elif s == 7:
    print('Sábado')
else:
    print('Inválido')
