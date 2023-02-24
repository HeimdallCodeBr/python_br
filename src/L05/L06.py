# -*- coding: utf-8 -*-

"""Resolução Lista 05 Exercicio 06 Python Brasil (J.Siqueira 02/23)."""

"""
6. Faça um programa que converta da notação de 24 horas para a notação
de 12 horas.

Por exemplo, o programa deve converter 14:25 em 2:25 P.M.

A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
uma para fazer a conversão e uma para a saída.

Registre a informação A.M./P.M. como um valor "A" para A.M. e "P" para P.M.

Assim, a função para efetuar as conversões terá um parâmetro formal para
registrar se é A.M. ou P.M.

Inclua um loop que permita que o usuário repita
esse cálculo para novos valores de entrada todas as vezes que desejar.

"""


def verifica_entrada(verifica_hora: str):
    h1 = verifica_hora.replace(':', '').isdigit()
    h2 = int(verifica_hora[-2:])
    h3 = int(verifica_hora[:verifica_hora.find(':')])
    if h1 and h2 < 60 and h3 <= 23:
        return True
    else:
        return False


def converte_hora(hora_am: str):
    a = hora_am.find(':')
    b = int(hora_am[:a])
    if b > 12:
        b = b - 12
        return str(b)+hora_am[a:]+' PM'
    else:
        return str(b)+hora_am[a:]+' AM'


# ==================
# PROGRAMA PRINCIPAL
# ==================

while True:
    hora = input('Informe a hora no formato 24h "Ex: 23:45": ')
    if hora == '0':
        break
    else:
        if verifica_entrada(hora):
            print(converte_hora(hora))
            pass
        else:
            print('ERRO! digite novamente')
            input()
