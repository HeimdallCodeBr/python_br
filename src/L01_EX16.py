"""Resolução Lista 01 Exercicio 16 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

area = float(input('Qual a area a ser pintada em m²: '))

consumo_tinta = area/3

if consumo_tinta < 18:
    latas = 1
else:
    latas = int(consumo_tinta//18+1)

valor = latas * 80

print(f'\nconsumo.....: {consumo_tinta:.2f} litros')
print(f'\nlatas 18L...: {latas:.2f} unidade(s)')
print(f'\nvalor.......: {valor:.2f} R$')
