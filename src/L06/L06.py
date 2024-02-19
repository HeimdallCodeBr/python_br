# -*- coding: utf-8 -*-

"""Resolução Lista 06 Exercicio 06 Python Brasil (J.Siqueira 02/23)."""

"""
Data por extenso.
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do
usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973

Você nasceu em  29 de Outubro de 1973.

"""
data = input ('Informe data no formato dd/mm/aaaa: ')

dia, mes, ano = data.split('/')
mes_extenso = ''

if mes == '01':
    mes_extenso = 'Janeiro'
elif mes == '02':
    mes_extenso = 'Fevereiro'
elif mes == '03':
    mes_extenso = 'Março'
elif mes == '04':
    mes_extenso = 'Abril'
elif mes == '05':
    mes_extenso = 'Maio'
elif mes == '06':
    mes_extenso = 'Junho'
elif mes == '07':
    mes_extenso = 'Julho'
elif mes == '08':
    mes_extenso = 'Agosto'
elif mes == '09':
    mes_extenso = 'Setembro'
elif mes == '10':
    mes_extenso = 'Outubro'
elif mes == '11':
    mes_extenso = 'Novembro'
elif mes == '12':
    mes_extenso = 'Dezembro'


print(f'\nVocê nasceu em {dia} de {mes_extenso} de {ano}')
