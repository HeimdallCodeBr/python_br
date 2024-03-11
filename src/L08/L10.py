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
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel_naBomba):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel_naBomba = quantidadeCombustivel_naBomba

    def abastecerPorValor(self, valor_abastecer_real):
        "Método abastecer por valor"
        total_litros = valor_abastecer_real/self.valorLitro
        self.quantidadeCombustivel_naBomba -= total_litros
        return total_litros

    def abastecerPorLitro(self, quantidadeCombustivelLitro):
        "Método abastecer por litro"
        return quantidadeCombustivelLitro*self.valorLitro

    def alterarValor(self, novoValorLitro):
        "Método alterar valor do combustivél"
        self.valorLitro = novoValorLitro
        
    
    def alterarCombustivel(self):
        "Método alterar tipo do combustivel"

    def alterarQuantidadeCombustivel(self):
        "Método alterar quantidade do combustivel"

# Gasolina Comum: O preço médio é de R$ 5,57 por litro.
# Etanol Comum: O preço médio é de R$ 3,81 por litro.
# Diesel S10: O preço médio é de R$ 5,63 por litro.

b1 = bombaCombustivel('Gasolina', 5.57, 1200)
b2 = bombaCombustivel('Etanol', 3.81, 1500 )
b3 = bombaCombustivel('Disel', 5.63, 2500)



print(f'{b1.tipoCombustivel}')





















"""
class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        return litros_abastecidos

    def abastecer_por_litro(self, litros_abastecidos):
        valor_a_pagar = litros_abastecidos * self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        return valor_a_pagar

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel


# Example usage:
if __name__ == "__main__":
    bomba = BombaCombustivel(tipo_combustivel="Gasolina", valor_litro=4.5, quantidade_combustivel=1000)
    print(f"Initial quantity: {bomba.quantidade_combustivel} liters")
    litros_abastecidos = bomba.abastecer_por_valor(90)
    print(f"Liters filled: {litros_abastecidos:.2f}")
    print(f"Remaining quantity: {bomba.quantidade_combustivel:.2f} liters")
    valor_a_pagar = bomba.abastecer_por_litro(20)
    print(f"Amount to pay: ${valor_a_pagar:.2f}")
    bomba.alterar_valor(4.8)
    print(f"New value per liter: ${bomba.valor_litro:.2f}")
    bomba.alterar_combustivel("Etanol")
    print(f"New fuel type: {bomba.tipo_combustivel}")
    bomba.alterar_quantidade_combustivel(900)
    print(f"Updated quantity: {bomba.quantidade_combustivel:.2f} liters")






"""