# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 37 Python Brasil (J.Siqueira 03/21)."""

# Uma academia deseja fazer um senso entre seus clientes para descobrir
# o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você
# deve fazer um programa que pergunte a cada um dos clientes da academia
# seu código, sua altura e seu peso. O final da digitação de dados deve
# ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar
# o programa também deve ser informados os códigos e valores do cliente
# mais alto, do mais baixo, do mais gordo e do mais magro, além da média
# das alturas e dos pesos dos clientes.

import os 

os.system('clear')

i = 0
f = 40

matricula = []

altura = []
altura_menor_indice = 0
altura_menor = 1000
altura_maior_indice = 0
altura_maior = 0
altura_soma = 0
peso = []
peso_menor_indice = 0
peso_menor = 1000
peso_maior_indice = 0
peso_maior = 0
peso_soma = 0

print('='*f)
print('ACADEMIA TABAJARA')
print('='*f)

while True:

    a = int(input(f'Informe a matricula do cliente [{i}]: '))

    if a == 0:
        break

    b = float(input(f'Informe altura do cliente .....[{i}]: '))
    altura_soma += b
    
    if b > altura_maior:
        altura_maior = b
        altura_maior_indice = i
    
    if b < altura_menor:
        altura_menor = b
        altura_menor_indice = i

    c = float(input(f'Informe peso do cliente .......[{i}]: '))
    peso_soma += c
    
    if c > peso_maior:
        peso_maior = c
        peso_maior_indice = i
    
    if c < peso_menor:
        peso_menor = c
        peso_menor_indice = i
    
    print('-'*f)
    
    matricula.append(a)
    altura.append(b)
    peso.append(c)

    i+=1

print('\n')
print('\033[1;32m* * * * * * * * INDICES * * * * * * * * \033[1;m')
print(f'Média de altura...............: {altura_soma/i} cm')
print(f'Média de peso.................: {peso_soma/i} kg')
print('-'*f)
print(f'Matricula menor altura........: {matricula[altura_menor_indice]} ')
print(f'Menor altura..................: {altura[altura_menor_indice]} cm')
print(f'Matricula menor peso..........: {matricula[peso_menor_indice]} ')
print(f'Menor peso....................: {peso[peso_menor_indice]} kg')
print('-'*f)
print(f'Matricula maior altura........: {matricula[altura_maior_indice]} ')
print(f'Maior altura..................: {altura[altura_maior_indice]} cm')
print(f'Matricula maior peso..........: {matricula[peso_maior_indice]} ')
print(f'Maior peso....................: {peso[peso_maior_indice]} kg')
print('\n')    


# ========================================
# ACADEMIA TABAJARA
# ========================================
# Informe a matricula do cliente [0]: 15
# Informe altura do cliente .....[0]: 200
# Informe peso do cliente .......[0]: 97
# ----------------------------------------
# Informe a matricula do cliente [1]: 16
# Informe altura do cliente .....[1]: 207
# Informe peso do cliente .......[1]: 120
# ----------------------------------------
# Informe a matricula do cliente [2]: 17
# Informe altura do cliente .....[2]: 208
# Informe peso do cliente .......[2]: 96
# ----------------------------------------
# Informe a matricula do cliente [3]: 18
# Informe altura do cliente .....[3]: 201
# Informe peso do cliente .......[3]: 90
# ----------------------------------------
# Informe a matricula do cliente [4]: 0


# * * * * * * * * INDICES * * * * * * * * 
# Média de altura...............: 204.0 cm
# Média de peso.................: 100.75 kg
# ----------------------------------------
# Matricula menor altura........: 15 
# Menor altura..................: 200.0 cm
# Matricula menor peso..........: 18 
# Menor peso....................: 90.0 kg
# ----------------------------------------
# Matricula maior altura........: 17 
# Maior altura..................: 208.0 cm
# Matricula maior peso..........: 16 
# Maior peso....................: 120.0 kg
