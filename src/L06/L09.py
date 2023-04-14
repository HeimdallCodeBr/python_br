# -*- coding: utf-8 -*-

"""Resolução Lista 06 Exercicio 09 Python Brasil (J.Siqueira 02/23)."""

"""
Verificação de CPF.
Desenvolva um programa que solicite a digitação de um número de CPF no
formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através
da validação dos dígitos verificadores e dos caracteres de formatação.

"""


cpf = '252.516.048-74'
cpf = cpf.replace('.', '')

cpf_digitos = ''
cpf_verificador = ''
cpf_verificador_calculado = ''
soma_verificador_1 = 0
soma_verificador_2 = 0

cpf_digitos, cpf_verificador = cpf.split('-')
cpf_digitos = cpf_digitos[::-1]


# CALCULO DO PRIMEIRO DIGITO VERIFICADOR
# ======================================

for d1 in reversed(range(2, len(cpf_digitos)+2)):
    soma_verificador_1 += int(cpf_digitos[d1-2]) * d1

if soma_verificador_1 % 11 < 2:
    digito_1 = 0
else:
    digito_1 = 11 - soma_verificador_1 % 11

cpf_digitos = cpf_digitos[::-1]
cpf_digitos += str(digito_1)

# CALCULO DO SEGUNDO DIGITO VERIFICADOR
# =====================================
cpf_digitos = cpf_digitos[::-1]

for d2 in reversed(range(2, len(cpf_digitos)+2)):
    soma_verificador_2 += int(cpf_digitos[d2-2]) * d2

if soma_verificador_2 % 11 < 2:
    digito_2 = 0
else:
    digito_2 = 11 - soma_verificador_2 % 11

cpf_verificador_calculado = str(digito_1) + str(digito_2)

if cpf_verificador == cpf_verificador_calculado:
    print('CPF é válido')
else:
    print('CPF não é válido')
