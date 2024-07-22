# pylint: disable=C0103

"""Resolução Lista 08 Exercicio 01 Python Brasil (J.Siqueira 02/23)."""

# -*- coding: utf-8 -*-

from os import system

# 1. Classe Bola:  Crie uma classe que modele uma bola:

# a. Atributos: Cor,  circunferência, material

# b. Métodos: trocaCor e mostraCor

system('cls')

class Bola:
    "Está classe representa uma bola."

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        self.cor_anterior = ''

    def troca_cor(self):
        "Troca a cor."
        cor_troca = input('Informe a nova cor: ')
        self.cor_anterior = self.cor
        self.cor = cor_troca.lower()
        return f'\nA cor foi alterada de "{self.cor_anterior}" para "{self.cor}"\n'

    def mostra_cor(self):
        "Mostra a cor."
        print(self.cor)


b1 = Bola('azul', '50', 'plástico')
b1.mostra_cor()

b1.troca_cor()''
b1.mostra_cor()
