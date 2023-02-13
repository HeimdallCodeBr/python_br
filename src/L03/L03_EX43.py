# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 43 Python Brasil (J.Siqueira 03/21)."""

# O cardápio de uma lanchonete é o seguinte:

# Especificação     Código      Preço
# Cachorro Quente   100         1,20
# Bauru Simples     101         1,30
# Bauru com ovo     102         1,50
# Hambúrguer        103         1,30
# Cheeseburguer     104         1,20
# Refrigerante      105         1,00

# Faça um programa que leia o código dos itens pedidos e as quantidades 
# desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade)
# e o total geral do pedido. Considere que o cliente deve informar quando o 
# pedido deve ser encerrado.

import os
os.system('clear')

lista_produto = ['Cachorro Quente',
                 'Bauru Simples',
                 'Bauru com ovo',
                 'Hambúrger',
                 'Cheeseburguer',
                 'Refrigerantes']

lista_codigo = [100, 101, 102, 103, 104, 105]
lista_preco = [1.20, 1.30, 1.50, 1.30, 1.20, 1.00]

# Recebe pedido com base na posição da lista
lista_i = []
lista_pedido = []
lista_pedido_produto = []
lista_quantidade = []
lista_valor = []
soma_pedido = 0

i = 0
f = 57

print('\033[1;32mENTRADA DO PEDIDO\033[1;m')

while True:
    print('-'* f)      
    pedido = int(input(f'[{i}] Informe o código do produto: '))
    if pedido != 0:
        lista_i.append(i)
        lista_pedido.append(pedido)
        lista_pedido_produto.append(lista_produto[(lista_codigo.index(pedido))])
    else:
        break
    quantidade = int(input(f'[{i}] Informe a quantidade.......: '))
    lista_quantidade.append(quantidade)
    lista_valor.append(quantidade * lista_preco[lista_codigo.index(pedido)])
    i += 1

print('\n')
print('='* f)
print('\033[1;32mRESUMO DO PEDIDO\033[1;m')
print('='* f)
print(f'ITEM\tPRODUTO\t\t\tQUANTIDADE\tVALOR')
for k in range (len(lista_i)):
    soma_pedido += lista_valor[k]
    print('-'* f)
    print(f'{lista_pedido[k]}\t{lista_pedido_produto[k]}\t\t{lista_quantidade[k]}\t\tR$ {lista_valor[k]:,.2f}')
print('-'* f)
print(f'\t\t\t\tTotal a pagar:\t\033[1;44mR$ {soma_pedido:,.2f}\033[1;m')    
print('\n')


# ENTRADA DO PEDIDO
# ---------------------------------------------------------
# [0] Informe o código do produto: 105
# [0] Informe a quantidade.......: 10
# ---------------------------------------------------------
# [1] Informe o código do produto: 101
# [1] Informe a quantidade.......: 1
# ---------------------------------------------------------
# [2] Informe o código do produto: 102
# [2] Informe a quantidade.......: 3
# ---------------------------------------------------------
# [3] Informe o código do produto: 104
# [3] Informe a quantidade.......: 6
# ---------------------------------------------------------
# [4] Informe o código do produto: 103
# [4] Informe a quantidade.......: 2
# ---------------------------------------------------------
# [5] Informe o código do produto: 101
# [5] Informe a quantidade.......: 8
# ---------------------------------------------------------
# [6] Informe o código do produto: 0


# =========================================================
# RESUMO DO PEDIDO
# =========================================================
# ITEM    PRODUTO                 QUANTIDADE      VALOR
# ---------------------------------------------------------
# 105     Refrigerantes           10              R$ 10.00
# ---------------------------------------------------------
# 101     Bauru Simples           1               R$ 1.30
# ---------------------------------------------------------
# 102     Bauru com ovo           3               R$ 4.50
# ---------------------------------------------------------
# 104     Cheeseburguer           6               R$ 7.20
# ---------------------------------------------------------
# 103     Hambúrger               2               R$ 2.60
# ---------------------------------------------------------
# 101     Bauru Simples           8               R$ 10.40
# ---------------------------------------------------------
#                                 Total a pagar:  R$ 36.00