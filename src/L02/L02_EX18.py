# -*- coding: utf-8 -*-

"""Resolução Lista 02 Exercicio 18 Python Brasil (J.Siqueira 03/21)."""

# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
# mesma é uma data válida.
# JAN  01   31
# FEV  02   28
# MAR  03   31
# ABR  04   30
# MAI  05   31
# JUN  06   30
# JUL  07   31
# AGO  08   30
# SET  09   31
# OUT  10   30
# NOV  11   31
# DEZ  12   30

d = input('informe uma data: ').split('/')

dia = d[0]
mes = d[1]
ano = d[2]

va = False
vm = False

if len(ano) <= 4 and int(ano) >= 1900:
    va = True
    if mes == '02' and int(dia) <= 28:
        vm = True
    elif mes in '010305070911' and int(dia) <= 31:
        vm = True
    elif mes in '0406081012' and int(dia) <= 30:
        vm = True

if va is True and vm is True:
    print(f'\n\033[1;33mA data {"/".join(d)} é válida\033[1;m')
else:
    print(f'\n\033[1;31mA data {"/".join(d)} é inválida\033[1;m')
