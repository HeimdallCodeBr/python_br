# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 31 Python Brasil (J.Siqueira 03/21)."""

# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios
# de 1,99 e agora possui uma loja de conveniências. Faça um programa
# que implemente uma caixa registradora rudimentar. O programa deverá
# receber um número desconhecido de valores referentes aos preços das
# mercadorias. Um valor zero deve ser informado pelo operador para
# indicar o final da compra. O programa deve então mostrar o total da
# compra e perguntar o valor em dinheiro que o cliente forneceu, para
# então calcular e mostrar o valor do troco. Após esta operação, o
# programa deverá voltar ao ponto inicial, para registrar a próxima
# compra.

# A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...

import os
os.system('clear')

lista = []
i = 0
soma = 0
f = 35

while True:
    valor = float(input(f'Valor produto {i}: '))
    if valor != 0:
        lista.append(valor)
        i+=1
        soma +=valor
    else:
        os.system('clear')
        print('='*f)
        print('LOJAS TABAJARAS')
        print('='*f)

        for i in range(len(lista)):
            print(f'Produto: {str(i).zfill(3)}\t\tR$ {lista[i]}')
        print('-'*f) 
        print(f'Total\t\t\tR$ {soma:.2f}')
        print('\n')

        dinheiro = float(input('Informe o valor recebido pelo cliente: '))
        troco = dinheiro -  soma

        print('\n')
        print('*'*f)
        print('COMPROVANTE COMPRA')
        print('*'*f)
        print(f'Total\t\t\tR$ {soma:.2f}')
        print(f'Recebido\t\tR$ {dinheiro:.2f}')
        print(f'Troco\t\t\tR$ {troco:.2f}')
        print('-'*f)
        print('\n')
        input('pressione ENTER para continuar')
        os.system('clear')
        i = 0
        soma = 0
        lista = []






