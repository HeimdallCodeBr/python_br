# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 17 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios

# Faça um Programa que peça um número correspondente a um determinado ano e em
# seguida informe se este ano é ou não bissexto.

# Feitas as correções de calendário definiu-se a nova regra para o cálculo
# dos anos bissextos:
#   De 4 em 4 anos é ano bissexto.
#   De 100 em 100 anos não é ano bissexto.
#   De 400 em 400 anos é ano bissexto.
#   Prevalecem as últimas regras sobre as primeiras.[2]

# Para melhor entender

# São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
# São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não
# de 400, p.ex: 1996, 2000, 2004, 2008, 2012, 2016, 2020...
# Não são bissextos todos os demais anos.

ano = int(input('\nInforme ano: '))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('é ano bissexto')
else:
    print('não é ano bissexto')
