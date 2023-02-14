# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 17 Python Brasil (J.Siqueira 04/22)."""

# Em uma competição de salto em distância cada atleta tem direito a cinco
# saltos. O resultado do atleta será determinado pela média dos cinco valores
# restantes.
#
# Você deve fazer um programa que receba o nome e as cinco distâncias
# alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos
# e a média dos saltos. O programa deve ser encerrado quando não for informado
# o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#
# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
#
# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

from os import system

system('clear')

nome = []
texto = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
distancia = []
resultado = []
media = []

i = 0
s = 5
m = 0.0

while True:
    n = input('Informe o nome do atleta {}: '.format(i+1))
    if n != '':
        nome.append(n)
        i += 1
        for ds in range(s):
            d = float(
                input('Informe a distancia do salto {}/{}: '.format(ds+1, s)))
            distancia.append(d)
            m += d
    else:
        break

    resultado.append(distancia)
    distancia = []
    media.append(m / s)
    m = 0.0

f = (media.index(max(media)))
print(nome[f])
print(resultado[f])
print(media[f])
