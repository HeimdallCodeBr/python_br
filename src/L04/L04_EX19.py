# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 19 Python Brasil (J.Siqueira 04/22)."""

# Uma empresa de pesquisas precisa tabular os resultados da seguinte
# enquete feita a um grande quantidade de organizações:

# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado
# da enquete e informe ao final o resultado da mesma.
#
# O programa deverá ler os valores até ser informado o valor 0, que encerra
# a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa
# (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados
# num vetor. Após os dados terem sido completamente informados, o programa
# deverá calcular a percentual de cada um dos concorrentes e informar o
# vencedor da enquete. O formato da saída foi dado pela empresa, e é o
# seguinte:


# Sistema Operacional     Votos       %
# -------------------     -----       ---
# Windows Server          1500        17%
# Unix                    3500        40%
# Linux                   3000        34%
# Netware                 500         5%
# Mac OS                  150         2%
# Outro                   150         2%
# --------------------    ----
# Total                   8800


# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo
# a 40% dos votos.


from os import system
from random import randint

system('clear')
legenda: list = ['', '1- Windows Server', '2- Unix',
                 '3- Linux', '4- Netware', '5- Mac OS', '6- Outro']
sistema: list = []
votos: list = []
resultado: list = []
resultado_ordenado: list = []

v = 0

# while True:
#     system('clear')
#     print('Votos computados {}'.format(v))
#     print('======================')
#     print('1- Windows Server')
#     print('2- Unix')
#     print('3- Linux')
#     print('4- Netware')
#     print('5- Mac OS')
#     print('6- Outro')
#     print('Pressione 0 para sair')
#     print('======================')
#     voto = input('Qual o melhor Sistema Operacional para uso em servidores? ')
#     v += 1
#     if voto == '0':
#         v -= 1
#         break
#     else:
#         if voto.isdigit() and (int(voto) >= 1 and int(voto) <= 6):
#             if voto in sistema:
#                 votos[sistema.index(voto)] += 1
#             else:
#                 print(voto in sistema)
#                 sistema.append(voto)
#                 votos.append(1)
#         else:
#             v -= 1
#             print('Informe um valor entre 1 e 6 ou 0 para sair!')
#             input()


# ===================================
# HACK PARA GERAR NUMEROS ALEATORIOS
# ===================================
z = 0
for i in range(1300):
    a = randint(1, 6)
    b = randint(53, 99)
    z += 1
    if a in sistema:
        pass
    else:
        sistema.append(a)
        votos.append(b)
# ===================================

resultado.append(legenda[int(sistema[votos.index(max(votos))])])
resultado.append(max(votos))
resultado.append(max(votos)/sum(votos)*100)

x: list = []
for m, n in enumerate(sistema):
    x.append(legenda[int(n)])
    x.append(votos[m])
    x.append(votos[m]/sum(votos)*100)
    resultado_ordenado.append(x)
    x = []


print('\n')
print('Sistema Operacional     Votos        %')
print('-------------------     -----      ---')
resultado_ordenado.sort()

for m, n in enumerate(resultado_ordenado):
    r1 = resultado_ordenado[m][0][3:]
    r2 = resultado_ordenado[m][1]
    r3 = resultado_ordenado[m][2]
    print('{:<18}{:>11}{:>8.0f}%'.format(r1, r2, r3))
print('-------------------     -----      ---')
print('                          {} '.format(sum(votos)))
print('\n')
print('O Sistema Operacional mais votado foi o{}, com {} votos, correspondendo a {:.0f}% dos votos.'.format(
    resultado[0][2:], resultado[1], resultado[2]))
