# -*- coding: utf-8 -*-
from random import randint

"""Resolução Lista 05 Exercicio 11 Python Brasil (J.Siqueira 02/23)."""

"""
11. Data com mês por extenso.

Construa uma função que receba uma data no formato DD/MM/AAAA  e devolva
uma string no formato D de mesPorExtenso de AAAA.

Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

"""


def dataExtenso(data: str) -> str:
    data = data.replace('-', '/')
    data = data.replace('.', '/')
    d, m, a = data.split('/')
    dataDic = {
        '1': ['Janeiro', 31],
        '2': ['Fevereiro', 28, False],
        '3': ['Março', 31],
        '4': ['Abril', 30],
        '5': ['Maio', 31],
        '6': ['Junho', 30],
        '7': ['Julho', 31],
        '8': ['Agosto', 31],
        '9': ['Setembro', 30],
        '10': ['Outubro', 30],
        '11': ['Novembro', 30],
        '12': ['Dezembro', 31]
    }
    dias_mes = dataDic[str(int(m))][1]
    if int(d) <= dias_mes and len(a) > 2:
        return (f'{int(d)} de {dataDic[str(int(m))][0]} de {a}')
    else:
        return str(None)


# ==================
# PROGRAMA PRINCIPAL
# ==================

for i in range(15):
    d = randint(1, 51)
    m = randint(1, 12)
    a = randint(1970, 2023)
    data = (f'{str(d)}/{str(m).zfill(2)}/{a}')
    print(f'{data} = {dataExtenso(data)}')


print('10-10.11', dataExtenso('10-10.11'))
