# -*- coding: utf-8 -*-
# pylint: disable=C0103

"""Resolução Lista 08 Exercicio 04 Python Brasil (J.Siqueira 02/23)."""

import os

# 4. Classe Pessoa:  Crie uma classe que modele uma pessoa:
#       a. Atributos: nome, idade, peso e altura
#       b. Métodos: Envelhercer,  engordar,  emagrecer,  crescer.

# Obs:  Por padrão, a cada ano que nossa pessoa envelhece, sendo a
#       idade dela menor que 21 anos, ela deve crescer 0,5 cm.

os.system('cls')

class Pessoa():
    "Modela uma classe Pessoa."
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, ano):
        "Método envelhecer."
        self.idade += ano
        for a in range(ano):
            self.crescer()
        return self.idade

    def engordar(self, peso_add):
        "Método engordar."
        self.peso += peso_add
        return self.peso

    def emagrecer(self, peso_sub):
        "Método emagrecer."
        self.peso -= peso_sub
        return self.peso

    def crescer(self):
        "Método crescer."
        if self.idade <= 21:
            self.altura += 0.5


n1 = Pessoa('Jefersom', 16, 160, 190)
n2 = Pessoa('MJulia', 15, 50, 165)


for i in range(10):
    if n1.idade and n2.idade <= 21:
        print(i)
        n1.envelhecer(1)
        print(n1.nome, n1.idade, n1.altura)
        n2.envelhecer(1)
        print(n2.nome, n2.idade, n2.altura)
        print('--------------------------')
    else:
        break

