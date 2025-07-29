# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 23 Python Brasil (J.Siqueira 04/22)."""

# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de
# espaço em disco no seu servidor de arquivos.  Para tentar resolver este
# problema, o Administrador de Rede precisa saber qual o espaço ocupado
# pelos usuários, e identificar os usuários com maior espaço ocupado.
# Através de um programa, baixado da Internet, ele conseguiu gerar o
# seguinte arquivo, chamado "usuarios.txt":

# alexandre     456123789
# anderson      1245698456
# antonio       123456456
# carlos        91257581
# cesar         987458
# rosemary      789456125

# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste
# arquivo, você deve criar um programa que gere um relatório, chamado
# "relatório.txt", no seguinte formato:


# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr. Usuário             Espaço utilizado            % do uso
# 1 alexandre              434,99 MB                  16,85%
# 2 anderson              1187,99 MB                  46,02%
# 3 antonio                117,73 MB                   4,56%
# 4 carlos                  87,03 MB                   3,37%
# 5 cesar                    0,94 MB                   0,04%
# 6 rosemary               752,88 MB                  29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB

# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados
# em memória, caso sejam necessários, de forma a agilizar a execução do
# programa. A conversão da espaço ocupado em disco, de bytes para megabytes
# deverá ser feita através de uma função separada, que será chamada pelo
# programa principal. O cálculo do percentual de uso também deverá ser feito
#  através de uma função, que será chamada pelo programa principal.

from os import system

system('clear')

nome: list = []
utilizado: list = []
percentual: list = []
MB = 1024*1024
soma = 0.0
media = 0.0
m = 0

with open('src/L04/usuarios.txt') as arquivo:
    linhas = arquivo.readlines()

for i in (linhas):
    i = i.replace(' ', ',', 1)
    n, c = i.split(',')
    c = f'{float(c)/MB:.2f}'
    nome.append(n)
    utilizado.append(c)
    soma += float(c)


media = soma/len(nome)

with open('src/L04/relatorio.txt', 'w') as saida:
    saida.write('ACME Inc.            Uso do espaço em disco pelos usuários\n')
    saida.write(
        '------------------------------------------------------------------\n')
    saida.write('Nr.  Usuário             Espaço utilizado         % do uso\n')
    for k in range(len(nome)):
        c1 = str(k+1).ljust(5)
        c2 = nome[k].ljust(15)
        c3 = utilizado[k].rjust(12)
        c4 = float(utilizado[k])/soma*100
        saida.write(f'{c1}{c2}{c3} MB               {c4:.2f}%\n')
    saida.write('\n')
    saida.write('Espaço total ocupado: {:.2f} MB\n'.format(soma))
    saida.write('Espaço médio ocupado: {:.2f} MB\n'.format(media))
    saida.write('\n')


with open("src/L04/relatorio.txt", "r") as arquivo:
    print(arquivo.read())
