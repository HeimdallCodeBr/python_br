# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 41 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que receba o valor de uma dívida e mostre uma tabela
# com os seguintes dados: valor da dívida, valor dos juros, quantidade
# de parcelas e valor da parcela.

# Os juros e a quantidade de parcelas seguem a tabela abaixo:

# Quantidade de Parcelas | % de Juros sobre o valor inicial da dívida
# --------------------------------------------------------------------
# 1                      |                       0
# --------------------------------------------------------------------
# 3                      |                       10
# --------------------------------------------------------------------
# 6                      |                       15
# --------------------------------------------------------------------
# 9                      |                       20
# --------------------------------------------------------------------
# 12                     |                       25
# --------------------------------------------------------------------


import os
os.system('clear')

parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]
divida = []

valor = float(input('Informe o valor da divida: '))
print('\n')

for i in range (len(parcelas)):
    divida.append(valor+(valor*(juros[i]/100)))
    print(f'Parcelas: {parcelas[i]}\tJuros: {juros[i]}%\tValor parcela: R$ {divida[i]/parcelas[i]:,.2f}\tValor divida: R$ {divida[i]:,.2f}')
    print('-'*100)
print('\n')


# Informe o valor da divida: 1000

# Parcelas: 1     Juros: 0%       Valor parcela: R$ 1,000.00      Valor divida: R$ 1,000.00
# ----------------------------------------------------------------------------------------------------
# Parcelas: 3     Juros: 10%      Valor parcela: R$ 366.67        Valor divida: R$ 1,100.00
# ----------------------------------------------------------------------------------------------------
# Parcelas: 6     Juros: 15%      Valor parcela: R$ 191.67        Valor divida: R$ 1,150.00
# ----------------------------------------------------------------------------------------------------
# Parcelas: 9     Juros: 20%      Valor parcela: R$ 133.33        Valor divida: R$ 1,200.00
# ----------------------------------------------------------------------------------------------------
# Parcelas: 12    Juros: 25%      Valor parcela: R$ 104.17        Valor divida: R$ 1,250.00
# ----------------------------------------------------------------------------------------------------

