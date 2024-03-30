# -*- coding: utf-8 -*-
# pylint: disable=C0103
import os

# Resolução Lista 08 Exercicio 10 Python Brasil (J.Siqueira 02/23).


# 10. Classe Bomba de Combustível:
# Faça um programa completo utilizando classes e métodos que:

#   a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:

#       i. tipoCombustivel.

#       ii. valorLitro

#       iii. quantidadeCombustivel


#   b. Possua no mínimo esses métodos:

#       i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido
#          e mostra a quantidade de litros que foi colocada no veículo.

#       ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de
#           combustível e mostra o valor a ser pago pelo cliente.

#       iii. alterarValor( ) – altera o valor do litro do combustível.

#       iv. alterarCombustivel( ) – altera o tipo do combustível.

#       v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível
#          restante na bomba.


# OBS: Sempre e que acontecer um abastecimento é necessário atualizar a quantidade
#      de combustível total na bomba.


class bombaCombustivel():
    "Modelagem bomba de combustivel"
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel_naBomba):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel_naBomba = quantidadeCombustivel_naBomba

    def abastecerPorValor(self, valorParaAbastecer):
        "Método abastecer por valor"
        total_litros = valorParaAbastecer/self.valorLitro
        self.quantidadeCombustivel_naBomba -= total_litros
        return total_litros

    def abastecerPorLitro(self, litrosParaAbastecer):
        "Método abastecer por litro"
        self.quantidadeCombustivel_naBomba -= litrosParaAbastecer
        return litrosParaAbastecer * self.valorLitro

    def alterarValor(self, novoValorLitro):
        "Método alterar valor do combustivél"
        self.valorLitro = novoValorLitro

    def alterarCombustivel(self, novoCombustivel):
        "Método alterar tipo do combustivel"
        self.tipoCombustivel = novoCombustivel

    def alterarQuantidadeCombustivel(self, abasteceBombaLitros):
        "Método alterar quantidade do combustivel"
        self.quantidadeCombustivel_naBomba += abasteceBombaLitros


# 11/03/2024
# Gasolina Comum: O preço médio é de R$ 5,57 por litro.
# Etanol Comum: O preço médio é de R$ 3,81 por litro.
# Diesel S10: O preço médio é de R$ 5,63 por litro.

os.system('cls')

def mostraResumo():
    "Mostra resultado"
    print(f'{b1.tipoCombustivel}...: {b1.quantidadeCombustivel_naBomba:.1f} Litros')
    print(f'{b2.tipoCombustivel}.....: {b2.quantidadeCombustivel_naBomba:.1f} Litros')
    print(f'{b3.tipoCombustivel}......: {b3.quantidadeCombustivel_naBomba:.1f} Litros')
    print('--------------------------\n')



b1 = bombaCombustivel('Gasolina', 5.57, 1200)
b2 = bombaCombustivel('Etanol', 3.81, 1500 )
b3 = bombaCombustivel('Disel', 5.63, 2500)

mostraResumo()
print(f'{b1.tipoCombustivel} - {b1.abastecerPorValor(557):.2f} Litros\n')
mostraResumo()
print(f'{b3.tipoCombustivel} - {b3.abastecerPorValor(800):.2f} Litros\n')
mostraResumo()
print(f'{b1.tipoCombustivel} - {b1.abastecerPorLitro(100):.2f} R$\n')
mostraResumo()
b1.alterarValor(5.8)
print(f'{b1.tipoCombustivel} - {b1.abastecerPorValor(557):.2f} Litros\n')
mostraResumo()
b1.alterarQuantidadeCombustivel(96)
b2.alterarQuantidadeCombustivel(3500)
mostraResumo()
b1.alterarCombustivel('Gasolina Aditivada')
mostraResumo()
