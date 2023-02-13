# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 47 Python Brasil (J.Siqueira 04/22)."""

# Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos
# votos restantes. Você deve fazer um programa que receba o nome do ginasta
# e as notas dos sete  jurados  alcançadas  pelo  atleta  em  sua
# apresentação  e  depois  informe  a  sua  média,  conforme  a  descrição
# acima informada (retirar o melhor e o pior salto e depois calcular a média
# com as notas restantes). As notas não são informados ordenadas. Um exemplo
# de saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7
#
# Resultado final:
#
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

import os

os.system('clear')

c = 50
a = 0
jurados = 7
tabulado = {}
legenda = {0: 'Melhor nota', 1: 'Pior nota', 2: 'Média'}
nome_ganhador = ''
nota_ganhador = 0

while True:

    os.system('clear')
    print('='*c)
    print('COMPETIÇÃO DE GINASTICA')
    print('='*c)

    a += 1
    b = (f'\033[1;33m{str(a).zfill(2)}\033[1;m')
    atleta = input(f'Informe o nome do alteta [{b}]: ')
    print('-'*c)
    if atleta == '':
        break

    notas = []
    estatistica = []
    soma = 0
    media = 0
    melhor = 0
    pior = 99

    for i in range(jurados):
        b = (f'\033[1;32m{str(i+1).zfill(2)}\033[1;m')
        nota = float(input(f'Informe a nota [{b}]: '))

        if nota > melhor:
            melhor = nota

        if nota < pior:
            pior = nota

        soma += nota
        media = (soma - (melhor + pior))/5
        notas.append(nota)

    estatistica.append(melhor)
    estatistica.append(pior)
    estatistica.append(media)
    tabulado[atleta] = notas, estatistica

for i in tabulado:
    ganhador = tabulado[i][1][2]
    if ganhador > nota_ganhador:
        nota_ganhador = ganhador
        nome_ganhador = i

os.system('clear')
print('='*c)
print('ESTATISTICA')
print('='*c)

print(f'Atleta: \033[1;33m{nome_ganhador}\033[1;m')
print('-'*c)
for k in tabulado[nome_ganhador][0]:
    print(f'Nota.........: {k}')

print('-'*c)
print(f'\033[1;32mRESULTADO FINAL\033[1;m\n')
print(f'Atleta: \033[1;33m{nome_ganhador}\033[1;m')
for m in tabulado[nome_ganhador][1]:
    x = tabulado[nome_ganhador][1]
    y = x.index(m)
    print(f'{legenda[y]}: {m:.2f}')
print('\n')
print(tabulado)


# ENTRADA DE DADOS:

# {
# 'Sonia' : ([8.95, 8.92, 8.87, 8.72, 9.10, 8.21, 7.92], [9.10, 7.92, 8.734]),
# 'Julia' : ([8.63, 8.89, 8.72, 8.34, 9.50, 9.10, 8.88], [9.50, 8.34, 8.844]),
# 'Gisele': ([7.94, 7.32, 8.90, 8.57, 9.20, 9.70, 10.0], [10.0, 7.32, 8.862])
# }


# SAIDA DE DADOS:

# ==================================================
# ESTATISTICA
# ==================================================
# Atleta: Gisele
# --------------------------------------------------
# Nota.........: 7.94
# Nota.........: 7.32
# Nota.........: 8.9
# Nota.........: 8.57
# Nota.........: 9.2
# Nota.........: 9.7
# Nota.........: 10.0
# --------------------------------------------------
# RESULTADO FINAL

# Atleta: Gisele
# Melhor nota: 10.00
# Pior nota: 7.32
# Média: 8.86
