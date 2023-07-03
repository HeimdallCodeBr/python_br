# -*- coding: utf-8 -*-

import os

"""Resolução Lista 08 Exercicio 06 Python Brasil (J.Siqueira 02/23)."""

"""
6. Classe TV:

Faça um programa que simule um televisor criando-o como
um objeto.

O usuário deve ser capaz de informar o número do canal
e aumentar ou diminuir o volume.

Certifique-se de que o número do canal e o nível do volume permanecem
dentro de faixas válidas.

"""
os.system('clear')


class TV():

    def __init__(self, canal):
        self.canal = canal
        self.volume = 5

    def aumentar_volume(self):
        pass

    def diminuir_volume(self):
        pass

    def avancar_canal(self):
        pass

    def voltar_canal(self):
        pass

    def faixa_canal(self):
        if self.canal in range(100, 500):  # Faixa de canal entre 100 e 500
            print('Ok')
        else:
            print('canal fora do range')

    def faixa_volume(self):
        pass


samsung = TV(8)

print(samsung.faixa_canal(99))
