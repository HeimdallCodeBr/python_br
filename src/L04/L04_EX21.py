# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 21 Python Brasil (J.Siqueira 04/22)."""

# Faça um programa que carregue uma lista com os modelos de cinco carros
# (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista
# com o consumo desses carros, isto é, quantos quilômetros cada um desses
# carros faz com um litro de combustível. Calcule e mostre:

# a. O modelo do carro mais econômico;
# b. Quantos litros de combustível cada um dos carros cadastrados consome
#    para percorrer uma distância de 1000 quilômetros e quanto isto custará,
#    considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma
#    tela de exemplo. O disposição das informações deve ser o mais próxima
#    possível ao exemplo. Os dados são fictícios e podem mudar a cada execução
#    do programa.

# Comparativo de Consumo de Combustível
# Veículo 1
# Nome: fusca
# Km por litro: 7

# Veículo 2
# Nome: gol
# Km por litro: 10

# Veículo 3
# Nome: uno
# Km por litro: 12.5

# Veículo 4
# Nome: Vectra
# Km por litro: 9

# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5

# Relatório Final

# 1 - fusca   - 7.0   -   142.9 litros - R$ 321.43
# 2 - gol     - 10.0  -   100.0 litros - R$ 225.00
# 3 - uno     - 12.5  -   80.0  litros - R$ 180.00
# 4 - vectra  - 9.0   -   111.1 litros - R$ 250.00
# 5 - peugeout- 14.5  -   69.0  litros - R$ 155.17

# O menor consumo é do peugeout.

from os import system

system('clear')
veiculo = []
veiculos = []
consumo = []
v = 0
nome = ''
km_l = 0.0


while v < 5:
    print('Veiculo: {}'.format(v+1))
    nome = input('Nome: ')
    km_l = float(input('km/l: '))
    print('-------------------------------')
    v += 1
    veiculo.append(v)
    veiculos.append(nome)
    consumo.append(km_l)


# veiculo = [1, 2, 3, 4, 5]
# veiculos = ['Renault Kwid', 'GM Onix', 'Fiat Argo', 'GMT Turbo', 'Fiat Mobi']
# consumo = [15.2, 18.3, 14.2, 14.9, 24.5]

print('\n')
print('Relatório Final')
print('---------------')

for i in range(len(veiculos)):
    litros = 1000/consumo[i]
    gasto = litros * 2.25
    print('{:<1} - {:<12} - {:<5}km/l - {:.0f} litros - R$ {:.2f}'.format(
        veiculo[i], veiculos[i], consumo[i], litros, gasto))

print('\nO menor consumo é do {}\n'.format(
    veiculos[consumo.index(max(consumo))]))
