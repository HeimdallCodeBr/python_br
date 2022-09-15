# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 38 Python Brasil (J.Siqueira 03/21)."""

# Um funcionário de uma empresa recebe aumento salarial anualmente:

# Sabe-se que:

# a. Esse funcionário foi contratado em 1995, com salário inicial
#    de R$ 1.000,00;

# b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;

# c. A partir de 1997 (inclusive), os aumentos salariais sempre
#    correspondem ao dobro do percentual do ano anterior.

# Faça um programa que determine o salário atual desse funcionário.

# Após concluir isto, altere o programa permitindo que o usuário
# digite o salário inicial do funcionário.

import datetime
import os

os.system('clear')

ano_final = datetime.datetime.now().year
ano = 1996

salario = float(input('Digite o salário do funcionário: '))
aumento = float(input('Informe o % aumento a ser dado: '))

aumento = 1 + (aumento/100)

while ano <= ano_final:
    salario *= aumento
    print(f'Ano: {ano}\t R$ {salario:,.2f}')
    ano += 1
