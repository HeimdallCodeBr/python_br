# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 3 Python Brasil (J.Siqueira 03/21)."""

# Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v', 'd';

while True:
    i = 0

    print("\n")
    nome = input("Informe um nome......: ")
    idade = input("Informe a idade......: ")
    salario = input("Informe o salário....: ")
    sexo = input("Informe o sexo.......: ")
    estado = input("Informe estado civil.: ")

    if (nome.isnumeric() == False) and (len(nome) >= 3):
        i += 1
    if (idade.isnumeric() == True) and (int(idade) > 0 and int(idade) <= 150):
        i += 1
    if (salario.isnumeric() == True) and (int(salario) >= 0):
        i += 1
    if sexo.lower() in "fm":
        i += 1
    if estado.lower() in "scvd":
        i += 1

    if i < 5:
        print(f"\033[1;31m{5-i} erro(s) encontrado(s)! Digite novamente\033[1;m\n")
    else:
        print("\033[1;32mValidação realizada com sucesso\033[1;m\n")
        break
