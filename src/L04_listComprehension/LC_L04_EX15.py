# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 15 Python Brasil (J.Siqueira 04/22)."""

# Faça um programa que leia um número indeterminado de valores,
# correspondentes a notas, encerrando a entrada de dados quando
# for informado um valor igual a -1 (que não deve ser armazenado).
#
# Após esta entrada de dados, faça:

# a. Mostre a quantidade de valores que foram lidos;

# b. Exiba todos os valores na ordem em que foram informados, um
#    ao lado do outro;

# c. Exiba todos os valores na ordem inversa à que foram informados,
#    um abaixo do outro;

# d. Calcule e mostre a soma dos valores;

# e. Calcule e mostre a média dos valores;

# f. Calcule e mostre a quantidade de valores acima da média calculada;

# g. Calcule e mostre a quantidade de valores abaixo de sete;

# h. Encerre o programa com uma mensagem;


from os import system

system('clear')

i = 0
notas = []
notas1 = []
notas2 = []
cab = 60
soma = 0.0

print('='*cab)
print('ENTRADA NOTA - PARA SAIR DIGITE O VALOR -1')
print('='*cab)
while True:
    valor = float(input(f'Informe numero [{i+1}]: '))
    print('-'*cab)
    i += 1

    if valor == -1:
        break
    else:
        notas.append(valor)
        soma += valor

a = len(notas)
b = notas
c = notas[::-1]
d = soma
e = d/a

for k in (notas):
    if k > e:
        notas1.append(k)
    elif k < 7:
        notas2.append(k)

f = notas1
g = notas2

print('\n')
print('='*cab)
print('SAIDA DO PROGRAMA')
print('='*cab)
print(f'a. Quantidade de valores.....: {a}')
print(f'b. Valores na ordem digitados: {b:}')
print(f'c. Valores na ordem reversa..: {c:}')
print(f'd. Soma dos valores..........: {d}')
print(f'e. Média dos valores.........: {e}')
print(f'f. Valores acima da média....: {f}')
print(f'g. Valores abaixo de 7.0.....: {g}')
print('\n')
print('MENSAGEM: * * * FIM DO PROGRAMA * * *')
print('\n')


# =============================================
# ENTRADA NOTA - PARA SAIR DIGITE O VALOR -1
# =============================================
# Informe numero [1]: 7
# ---------------------------------------------
# Informe numero [2]: 2
# ---------------------------------------------
# Informe numero [3]: 4
# ---------------------------------------------
# Informe numero [4]: 2
# ---------------------------------------------
# Informe numero [5]: 8
# ---------------------------------------------
# Informe numero [6]: 7
# ---------------------------------------------
# Informe numero [7]: 8
# ---------------------------------------------
# Informe numero [8]: 9
# ---------------------------------------------
# Informe numero [9]: 8
# ---------------------------------------------
# Informe numero [10]: 1
# ---------------------------------------------
# Informe numero [11]: -1
# ---------------------------------------------


# =============================================
# SAIDA DO PROGRAMA
# =============================================
# a. Quantidade de valores.....: 10
# b. Valores na ordem digitados: [7.0, 2.0, 4.0, 2.0, 8.0, 7.0, 8.0, 9.0, 8.0,
#                                 1.0]
# c. Valores na ordem reversa..: [1.0, 8.0, 9.0, 8.0, 7.0, 8.0, 2.0, 4.0, 2.0,
#                                 7.0]
# d. Soma dos valores..........: 56.0
# e. Média dos valores.........: 5.6
# f. Valores acima da média....: [7.0, 8.0, 7.0, 8.0, 9.0, 8.0]
# g. Valores abaixo de 7.0.....: [2.0, 4.0, 2.0, 1.0]


# MENSAGEM: * * * FIM DO PROGRAMA * * *
