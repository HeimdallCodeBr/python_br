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
a = ''
i = 0
s = 5
m = 0.0

nome = ['Joaquim', 'Pedro', 'Laerte']
resultado = [[3.45, 3.68, 3.46, 3.38, 3.54], [
    3.47, 3.39, 3.48, 3.58, 3.61], [3.2, 3.6, 3.49, 3.38, 3.68]]
media = [3.502, 3.506, 3.490]


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


system('clear')
f = (media.index(max(media)))
print('Atleta: {}'.format(nome[f]))

for i, t in enumerate(texto):
    print('{} salto: {} m'.format(t, resultado[f][i]))
    a = a + ' - ' + str(resultado[f][i])

print('\n')
print('RESULTADO FINAL:')
print('Atleta: {}'.format(nome[f]))

a = a[3:]
print('Saltos: {}'.format(a))
print('Média dos saltos: {} m'.format(media[f]))
