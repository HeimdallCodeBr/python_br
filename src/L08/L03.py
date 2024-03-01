# -*- coding: utf-8 -*-
# pylint: disable=C0103

"""Resolução Lista 08 Exercicio 03 Python Brasil (J.Siqueira 02/23)."""

from os import system

# 3. Classe Retangulo:  Crie uma classe que modele um retangulo:
#       a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base
#          e Altura, a escolher);
#       b. Métodos: Mudar valor dos lados, Retornar valor dos lados,
#          calcular Área e calcular Perímetro;
#       c. Crie um programa que utilize esta classe. Ele deve pedir
#          ao usuário que informe as medidades de um local.
#          Depois, deve criar um objeto com as medidas e calcular a
#          quantidade de pisos e de rodapés necessárias para o local.

system('cls')


class Retangulo():
    "Modela uma classe Retangulo."
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_valor(self, lado_a_modificado, lado_b_modificado):
        "Altera o valor das areas do retangulo."
        self.lado_a = lado_a_modificado
        self.lado_b = lado_b_modificado

    def retornar_valor(self):
        "Retorna o valor dos lados do retangulo."
        return self.lado_a, self.lado_b

    def calcular_area(self):
        "Retorna a areada do retangulo."
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        "Retorna o perimetro do retangulo."
        return 2 * (self.lado_a + self.lado_b)


if __name__ == '__main__':

    r1 = Retangulo(50, 40)  # area 200, perimetro 60
    r2 = Retangulo(40, 30)  # area 1200, perimetro 140
    r3 = Retangulo(30, 10)  # area 300, perimetro 80

    print('-------------------')
    print('Altera Valor')
    print(r1.retornar_valor())
    r1.mudar_valor(10, 20)
    print(r1.retornar_valor())
    print('-------------------')
    print('Calcula Area')
    print(r1.calcular_area())
    print(r2.calcular_area())
    print(r3.calcular_area())
    print('-------------------')
    print('Calcula Perimetro')
    print(r1.calcular_perimetro())
    print(r2.calcular_perimetro())
    print(r3.calcular_perimetro())
