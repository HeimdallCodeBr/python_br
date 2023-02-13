# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 46 Python Brasil (J.Siqueira 04/22)."""

# Em uma competição de salto em distância cada atleta tem direito a cinco
# saltos. No final da série de saltos de cada atleta, o melhor e o pior
# resultados são eliminados. O seu resultado fica sendo a média dos três
# valores restantes. Você deve fazer um programa que receba o nome e as
# cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
# a média dos saltos conforme a descrição acima informada (retirar o melhor
# e o pior salto e depois calcular a média). Faça uso de uma lista para
# armazenar os saltos. Os saltos são informados na ordem da execução,
# portanto não são ordenados. O programa deve ser encerrado quando não
# for informado o nome do atleta. A saída do programa deve ser conforme o
# exemplo abaixo:

# Atleta: Rodrigo Curvêllo 

# Primeiro Salto: 6.5 m 
# Segundo Salto: 6.1 m 
# Terceiro Salto: 6.2 m 
# Quarto Salto: 5.4 m 
# Quinto Salto: 5.3 m 

# Melhor salto:  6.5 m 
# Pior salto: 5.3 m 
# Média dos demais saltos: 5.9 m 
# Resultado final: 
# Rodrigo Curvêllo: 5.9 m

import os
os.system('clear')

c = 40
estatistica = {}
legenda = { 0: 'Primeiro', 1: 'Segundo', 2: 'Terceiro', 3: 'Quarto', 4: 'Quinto'}
legenda2 = {0: 'Melhor', 1: 'Pior', 2: 'Média'}
final_distancia = 0
final_nome = ''


while True:
    os.system('clear')
    print ('='*c)    
    print ('COMPETIÇÃO SALTO EM DISTANCIA')
    print ('='*c)
    
    atleta = input('Informe o nome do atleta: ')
    print('-'*c)
    if atleta == '':
        break
    
    salto = []
    resultado = []
    media = 0
    melhor = 0
    pior = 999
    total = 0
    final_distancia = 0

    for i in legenda:
        distancia = float(input(f'Informe a distancia do {legenda[i]} salto: '))
        salto.append(distancia)
        total += distancia

        if distancia > melhor:
            melhor = distancia

        if distancia < pior:
            pior = distancia
            
    media = (total - (melhor+pior))/3

    resultado.append(melhor)
    resultado.append(pior)
    resultado.append(media)
        
    estatistica[atleta] = salto, resultado

for k in estatistica:
    valor_melhor_media = estatistica[k][1][2]
    
    if valor_melhor_media > final_distancia:
        final_distancia = valor_melhor_media
        final_nome = k

os.system('clear')
print ('='*c)    
print ('RESULTADO FINAL')
print ('='*c)
print (f'Nome do Atleta: {final_nome}')
print ('-'*c)
for m in estatistica[final_nome][0]:
    x = estatistica[final_nome][0]
    y = x.index(m)
    print (f'{legenda[y]} Salto: {m}m')

print ('-'*c)

for m in estatistica[final_nome][1]:
    x = estatistica[final_nome][1]
    y = x.index(m)
    print (f'{legenda2[y]} Salto: {m:.2f}m')

print ('-'*c)
print ('Resultado Final')
print (f'{final_nome}: {final_distancia:.2f}m')


# ========================================
# RESULTADO FINAL
# ========================================
# Nome do Atleta: Jefersom
# ----------------------------------------
# Primeiro Salto: 1.89m
# Segundo Salto: 1.88m
# Terceiro Salto: 1.91m*
# Quarto Salto: 1.47m*
# Quinto Salto: 1.58m
# ----------------------------------------
# Melhor Salto: 1.91m
# Pior Salto: 1.47m
# Média Salto: 1.78m
# ----------------------------------------
# Resultado Final
# Jefersom: 1.78m