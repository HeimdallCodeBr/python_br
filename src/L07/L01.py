# -*- coding: utf-8 -*-

"""Resolução Lista 07 Exercicio 01 Python Brasil (J.Siqueira 02/23)."""

from os import system


"""
1. Faça um programa que leia um arquivo texto contendo uma lista de
endereços IP e gere um outro arquivo, contendo um relatório dos endereços
IP válidos e inválidos.

O arquivo de entrada possui o seguinte formato:

200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256

"""
system('clear')


# Função ler arquivo .txt
def le_txt(arquivo):
    lista = []
    with open(arquivo, "r") as txt:
        conteudo = txt.read()
    for c in conteudo.split('\n'):
        lista.append(c)
    return lista

# Função gravar arquivo .txt
def grava_txt(item):
    



# ---------------------
# PROGRAMA PRINCIPAL
# ---------------------

relacao_ip = le_txt('src/L07/ip.txt')


print(relacao_ip)

validos: list = []
invalidos: list = []
valido = True

for i in relacao_ip:


    for k in i.split('.'):
        if k <= 255:
            valido = True
        else:
            valido =  False