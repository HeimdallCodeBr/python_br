# -*- coding: utf-8 -*-

from os import system


"""Resolução Lista 08 Exercicio 01 Python Brasil (J.Siqueira 02/23)."""

"""
1. Classe Bola:  Crie uma classe que modele uma bola:

a. Atributos: Cor,  circunferência, material

b. Métodos: trocaCor e mostraCor

"""

system('clear')


class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self):
        cor_troca = input('Informe a nova cor: ')
        self.cor_anterior = self.cor
        self.cor = cor_troca.lower()
        print(f'\nA cor foi alterada de "{self.cor_anterior}" para "{self.cor}"\n')

    def mostra_cor(self):
        print(self.cor)


b1 = Bola('azul', '50', 'plástico')
b1.mostra_cor()

b1.troca_cor()
b1.mostra_cor()