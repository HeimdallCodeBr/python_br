# -*- coding: utf-8 -*-

import os
"""Resolução Lista 08 Exercicio 02 Python Brasil (J.Siqueira 02/23)."""

"""
2. Classe Quadrado:  Crie uma classe que modele um quadrado:

a. Atributos: Tamanho do lado

b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

"""

os.system('clear')


class Quadrado():

    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
    
    def muda_valor_lado(self):
        novo_valor_lado = input('Informe o novo valor: ')
        self.tamanho_lado = novo_valor_lado

    def retorna_valor_lado(self):
        print(f'\nValor do tamanho do lado: {self.tamanho_lado}\n')

    def calcular_area(self):
        area = int(self.tamanho_lado) * int(self.tamanho_lado)
        print(f'Valor da área é {area}')


q1 = Quadrado(8)

q1.retorna_valor_lado()
q1.muda_valor_lado()
q1.retorna_valor_lado()
q1.calcular_area()
