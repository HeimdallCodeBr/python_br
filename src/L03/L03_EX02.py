# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 2 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que leia um nome de usuário e a sua senha e não
# aceite a senha igual ao nome do usuário, mostrando uma mensagem
# de erro e voltando a pedir as informações.

while True:
    nome = input("Informe um nome....: ")
    senha = input("Informe uma senha..: ")

    if nome == senha:
        print("\nErro!")
    else:
        print("\nUsuário Logado")
        break
