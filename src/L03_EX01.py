# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 1 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continuepedindo até que o usuário informe um valor válido.

while True:
    n = input("Informe uma nota válida: ")

    if n.isnumeric() and int(n) <= 10:
        print("nota válida")
        break
    else:
        print("nota inválida, digite novamente")
