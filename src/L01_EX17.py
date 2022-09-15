"""Resolução Lista 01 Exercicio 17 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

# Faça um Programa para uma loja de tintas.

# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
# preços em 3 situações:

# comprar apenas latas de 18 litros;

# comprar apenas galões de 3,6 litros;

# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
# considere latas cheias.


# Qual a area a ser pintada em m²: 1000
# consumo.....: 183.33 litros
# latas 18L...: 11.00 unidade(s)
# galão 3.6L..: 51.00 unidade(s)
# valorG......: 1275.00 R$
# valorL......: 880.00 R$


# Qual a area a ser pintada em m²: 895.89
# Consumo de tinta....: 164.0 litro(s)
# OPÇÃO 1 - comprar apenas latas de 18L
# latas 18L....: 10.0 unidade(s)
# valor........: 800.00 R$


area = float(input('Qual a area a ser pintada em m²: '))
consumo_tinta = (area * 1.1) // 6
print(f'Consumo de tinta....: {consumo_tinta:.1f} litro(s)')
print('==========================================')

# Opção 1 - comprar apenas latas de 18L

if consumo_tinta <= 18:
    latas = 1
else:
    latas = int(consumo_tinta // 18)
valorL = latas * 80

print('\nOPÇÃO 1 - comprar apenas latas de 18L \n')
print(f'latas 18L....: {latas} unidade(s)')
print(f'valor........: {valorL:.2f} R$')
print('\n==========================================\n')

# Opção 2 - comprar apenas galões de 3.6L

if consumo_tinta <= 3.6:
    galoes = 1
else:
    galoes = int(consumo_tinta // 3.6)
valorG = latas * 25

print('OPÇÃO 2 - comprar apenas galões de 3.6L \n')
print(f'latas 3.6L...: {galoes} unidade(s)')
print(f'valor........: {valorG:.2f} R$')
print('\n==========================================\n')


# Opção 3 - mix entre latas 18L e galões de 3.6L menor desperdício
restante = 0
if consumo_tinta <= 18:
    latas = 1
    if consumo_tinta > 18:
        galoes = int(consumo_tinta // 18)
        restante = int(consumo_tinta // 18 - consumo_tinta / 18)

valorG = latas * 25

print('OPÇÃO 3 - mix entre latas 18L e galões de 3.6L menor desperdício \n')
print(f'latas 18L....: {galoes} unidade(s)')
print(f'restante.....: {restante:.5f} litro(s)')
print(f'valor........: {valorG:.2f} R$')
print('\n==========================================\n')
