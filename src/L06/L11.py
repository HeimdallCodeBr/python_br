# -*- coding: utf-8 -*-

from os import system

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
-> Você errou pela 2ª vez. Tente de novo!

"""

system("clear")

palavra = "laranja"
palavra_secreta = ""
letra = "a"

for i, j in enumerate(palavra):
    print(i, j)
