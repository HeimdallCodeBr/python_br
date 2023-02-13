"""Resolução Lista 01 Exercicio 06 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

from math import pi

t = 'CALCULO DA AREA DA CIRCUNFERENCIA'
# A = 3,1416*r^2
print(f'{t:*^95}', end='\n\n')

r = float(input('Digite o raio da circunferência em cm: '))
a = pi*(r**2)
print(f'\nO valor em {r}cm convertido é de {a:.1f}cm²')
