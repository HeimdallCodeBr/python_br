# pylint: disable=W0105, C0103, C0116


# -*- coding: utf-8 -*-

"""Resolução Lista 07 Exercicio 01 Python Brasil (J.Siqueira 06/23)..."""

import os
import datetime

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
os.system('clear')

# Função para ler o arquivo e transformar em uma lista
#   1. Verificar se o arquivo de entrada existe no diretorio corrente;


def le_txt(arquivo):
    # shutil.os.remove('saida.txt')
    lista = []
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as registros:
            ips = registros.read()
        for ip in ips.strip().split('\n'):
            lista.append(ip)
        return lista
    else:
        if not os.path.exists(arquivo):
            return lista

# Função para classifica a validade do IP em VÁLIDOS e INVÁLIDOS
#   1. Verifica se existe conteudo dentro do arquivo;
#   2. Remove os espaços em brancos;
#   3. Verifica se atende a estrutura de 4 conjuntos/3 digitos entre 0 - 255;
#   4. Saida é gera uma tupla com IPs válidos e inválidos;


def verifica_ip(lista):
    approved = []
    disapproved = []
    e = 0  # error length
    v = 0  # validated
    for ip in lista:
        v = 0
        e = 0
        for i in ip.split('.'):  # verifica se IP tem 4 conjuntos de 32 bits
            v += 1
            if int(i) < 0 or int(i) > 255:  # verifica os valores entre 0 - 255
                e += 1
        if v == 4 and e == 0:
            approved.append(ip)
        else:
            disapproved.append(ip)
    return approved, disapproved

# Função gera arquivo de saida;
#   1. Inclui cabeçalho: [Endereços válidos:]
#   2. Grava os IPs válidos
#   3. Pula 2 linhas em braco
#   4. Inclui cabeçalho: [Endereços inválidos:]


def relatorio_txt(tupla_ip):
    if len(tupla_ip[0]) <= 0 and len(tupla_ip[1]) <= 0:
        print('não há registros carregados')
    else:
        for i, ip in enumerate(tupla_ip):
            g = False
            if i == 0 and g is False:
                grava_txt('saida.txt', '[Endereços Válidos]')
                g = True
            if i == 1 and g is False:
                grava_txt('saida.txt', '\n[Endereços Inválidos]')
                g = True
            for k in ip:
                grava_txt('saida.txt', k)
    return True


# Grava os registros no arquivo SAIDA.txt

def grava_txt(arquivo, registro):
    with open(arquivo, 'a') as registros:
        registros.write(f'{registro}\n')

# Função principal


def relatorio_ip(arquivo):
    a = le_txt(arquivo)
    b = verifica_ip(a)
    relatorio_txt(b)
    foot = f'\n\nRelatório gerado em: {datetime.datetime.now()}'
    grava_txt('saida.txt', foot)
    return True


# -----------------------------------
# PRINCIPAL
# -----------------------------------

relatorio_ip('ip.txt')






        

