# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 29 Python Brasil (J.Siqueira 03/21)."""

# O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99,
# com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente
# deve pagar ele desenvolveu um tabela que contém o número de itens que o
# cliente comprou e ao lado o valor da conta. Desta forma a atendente do
# caixa precisa apenas contar quantos itens o cliente está levando e olhar
# na tabela de preços. Você foi contratado para desenvolver o programa que
# monta esta tabela de preços, que conterá os preços de 1 até 50 produtos,
# conforme o exemplo abaixo:
#
# Lojas Quase Dois      Tabela de preços
#               01      R$ 1.99
#               02      R$ 3.98
#                   ...
#               50      R$ 99.50

import os

os.system('clear')

print('='*35)
print(f'Loja Quase Dois - TABELA DE PREÇOS')
print('='*35)

for i in range(50):
    print(f'{str(i+1).zfill(2)} - R$ {(i+1)*1.99:.2f}')
    print('-'*35)
print('='*35)