# pylint: disable=W0105, W1514, C0114, C0103

# -*- coding: utf-8 -*-

from os import system
import random

"""Resolução Lista 06 Exercicio 11 Python Brasil (J.Siqueira 02/23)."""

"""
Jogo de Forca.

Desenvolva um jogo da forca.

O programa terá uma lista de palavras lidas de um arquivo
texto e escolherá uma aleatoriamente.

O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!
Digite uma letra: O
A palavra é: _ _ _ _ O
Digite uma letra: E
A palavra é: _ E _ _ O
Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo """

system("cls")

caminho = r"C:\Projetos\python_br\src\L06\palavras.txt"
with open(rf"{caminho}", "r") as arquivo:
    banco = arquivo.read()
    palavras = banco.split("\n")
    palavra_sorteada = random.choice(palavras)
    palavras.remove(palavra_sorteada)
    palavra_oculta = ""

# tentativas = 6
# print(palavra_sorteada)
# while tentativas >= 0:
#     letra = input("digite uma letra: ")
#     for i in palavra_sorteada:
#         if letra == i:
#             palavra_oculta += i
#         else:
#             palavra_oculta += "_"
#     print(palavra_oculta)


palavra_sorteada = "pipoca"
palavra_oculta = "_" * len(palavra_sorteada)


letra = "p"

p = 0
print(palavra_sorteada[:-1])
