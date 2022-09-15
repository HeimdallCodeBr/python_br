# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 40 Python Brasil (J.Siqueira 03/21)."""

# Foi feita uma estatística em cinco cidades brasileiras para coletar
# dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# a. Código da cidade;
# b. Número de veículos de passeio (em 1999);
# c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e. Qual a média de veículos nas cinco cidades juntas;
# f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

import os
os.system('clear')

cidade = ['Amazonas', 'São Paulo', 'Paraná   ', 'Rio Grande Sul', 'Espirito Santo']
veiculos = [2987, 1584, 1780, 2400, 2999]
acidentes = [1787, 6587, 1450, 657, 7458]

acidente_menor = 9999999999
acidente_maior = 0
veiculo_media = 0
acidente_media = 0
acidente_media_indice = 0

for i in range (len(cidade)):
    print(f'Cidades: {cidade[i]}\t\tVeiculos: {veiculos[i]}\t\tAcidentes: {acidentes[i]}')
    print('-'*75)

    if acidentes[i] < acidente_menor:
        acidente_menor = acidentes[i]
    if acidentes[i] > acidente_maior:
        acidente_maior = acidentes[i]

    if veiculos[i] < 2000:
        acidente_media += veiculos[i]
        acidente_media_indice += 1

    veiculo_media += veiculos[i]

print('\n')
print(f'Cidade: {cidade[acidentes.index(acidente_menor)]} menor taxa de acidentes: {acidente_menor}')
print('-'*75)
print(f'Cidade: {cidade[acidentes.index(acidente_maior)]} maior taxa de acidentes: {acidente_maior}')
print('-'*75)
print(f'Média de veiculos das capitais é {veiculo_media/len(cidade):,.0f}')
print('-'*75)
print(f'Média de acidentes com cidade com menos de 2,000 veiculos: {acidente_media/acidente_media_indice:,.0f} ({acidente_media_indice})')
print('\n')
