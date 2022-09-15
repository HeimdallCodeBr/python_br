# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 6 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que imprima na tela os números de 1 a 20, um abaixo
# do outro. Depois modifique o programa para que ele mostre os números
# um ao lado do outro.

print("\033[1;32m\n* * * * * Numeros um abaixo do outro * * * * *\033[1;m")
for i in range(1, 21):
    print(i)

print("\033[1;32m\n* * * * * Numero um do lado do outro * * * * *\033[1;m")
for i in range(1, 21):
    print(i, end=" ")

print("\n")
