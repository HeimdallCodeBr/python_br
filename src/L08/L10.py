# -*- coding: utf-8 -*-
# pylint: disable=C0103

"""Resolução Lista 08 Exercicio 10 Python Brasil (J.Siqueira 02/23)."""


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
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valorLitro):
        "Método abastecer por valor"
        return valorLitro

    def abastecerPorLitro(self):
        "Método abastecer por litro"

    def alterarValor(self, valorLitro):
        "Método alterar valor do combustivél"
        return valorLitro
    
    def alterarCombustivel(self):
        "Método alterar tipo do combustivel"

    def alterarQuantidadeCombustivel(self):
        "Método alterar quantidade do combustivel"

# Gasolina Comum: O preço médio é de R$ 5,57 por litro.
# Etanol Comum: O preço médio é de R$ 3,81 por litro.
# Diesel S10: O preço médio é de R$ 5,63 por litro.

g1 = bombaCombustivel('Gasolina', 5.57, 30)
print(g1.tipoCombustivel)
print(g1.valorLitro)
