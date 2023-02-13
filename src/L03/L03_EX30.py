# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 30 Python Brasil (J.Siqueira 03/21)."""

# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a 
# metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
# contratado para desenvolver o programa que monta a tabela de preços de pães, de 1
# até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

# Preço do pão: R$ 0.18

# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

import os

os.system('clear')

preco = float(input('Informe o valor unitário do pão: '))

print('='*30)
print(f'Preço do pão: R${preco}')
print('='*30)

for i in range(50):
    print(f'{str(i+1).zfill(2)} - R$ {(i+1)*preco:.2f}')
    print('-'*30)
print('='*30)