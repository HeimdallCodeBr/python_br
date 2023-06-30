# -*- coding: utf-8 -*-

import os

"""Resolução Lista 08 Exercicio 04 Python Brasil (J.Siqueira 02/23)."""

"""
4. Classe Pessoa:  Crie uma classe que modele uma pessoa:

a. Atributos: nome, idade, peso e altura

b. Métodos: Envelhercer,  engordar,  emagrecer,  crescer.

Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
sendo a idade dela menor que 21 anos, ela deve crescer
0,5 cm.

"""

os.system('clear')


class Pessoa():

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, ano):
        self.idade += ano
        return self.idade

    def engordar(self, peso_add):
        self.peso += peso_add
        return self.peso

    def emagrecer(self, peso_sub):
        self.peso -= peso_sub
        return self.peso

    def crescer(self, idade):
        pass


n1 = Pessoa('Jefersom', 47, 160, 1.90)
print(n1.nome)
print(n1.peso)
n1.engordar(3)
print(n1.peso)
n1.emagrecer(5)
print(n1.peso)
print(n1.idade)
n1.envelhecer(4)
print(n1.idade)
