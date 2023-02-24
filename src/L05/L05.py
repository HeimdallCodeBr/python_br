# -*- coding: utf-8 -*-

"""Resolução Lista 05 Exercicio 05 Python Brasil (J.Siqueira 02/23)."""

"""
5. Faça um programa com uma função chamada somaImposto.

A função possui dois parâmetros formais: taxaImposto, que é a quantia de
imposto sobre vendas expressa em porcentagem e o custo, que é o custo de
um item antes do imposto.  A função “altera” o valor de custo para incluir
o imposto sobre vendas.

"""


def somaImposto(custo: float, taxa: float) -> float:
    '''
    SomaImposto:
                função "altera" o valor do custo
                para incluir o imposto sobre vendas

    Parametros:
                custo (float): valor do custo do produto
                taxa (float): valor da taxa em percentual decimal
    Retorna:
                preco_atualizado (float): valor preço de venda com imposto

    '''
    return custo + (custo * taxa)


print(somaImposto(150, 0.022))
