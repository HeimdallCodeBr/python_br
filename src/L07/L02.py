# -*- coding: utf-8 -*-

"""Resolução Lista 07 Exercicio 02 Python Brasil (J.Siqueira 06/23)."""


import os

"""
2. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de
espaço em disco no seu servidor de arquivos.

Para tentar resolver este problema, o Administrador de Rede precisa saber
qual o espaço ocupado pelos usuários, e identificar os usuários com maior
espaço ocupa do. Através de um programa, baixado da Internet, ele conseguiu
gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
você deve criar um programa que gere um relatório, chamado "relatório.txt",
no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%
 
Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
memória, caso sejam necessários, de forma a agilizar a execução do programa.

A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser
feita através de uma função separada, que será chamada pelo programa principal.

O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal.

"""

os.system('clear')


with open('src/L07/usuario.txt') as registros:
    registro = registros.readlines()

usuario = {}
c1 = ''
c2 = ''
usuarios = 0.0
soma = 0.0
media = 0.0
for i in registro:
    c1 = i[:15].strip()
    c2 = i[16:].strip()
    c2_mb = float(c2)/1048576
    usuario[c1] = c2_mb
    usuarios += 1
    soma += float(c2_mb)


with open('src/L07/relatorio.txt', 'w') as saida:
    saida.write('ACME Inc.               Uso do espaço em disco pelos usuários')
    saida.write('\n------------------------------------------------------------------------\n')
    saida.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
    for m, k in enumerate(usuario.keys()):
        saida.write(f'{m:<4} {k:<10}{usuario[k]:>18.2f}{(usuario[k]/soma)*100:>15.2f}\n')
        media=(soma/usuarios)
    saida.write(f'\nEspaço total ocupado: {soma:.2f} MB')
    saida.write(f'\nEspaço médio ocupado: {media:.2f} MB')

