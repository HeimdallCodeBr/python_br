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
        pass

        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor_troca):
        pass

    def mostra_cor(self):
        print(self.cor)


b1 = Bola('azul', '50', 'plástico')

b1.mostra_cor()

