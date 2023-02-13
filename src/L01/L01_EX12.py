"""Resolução Lista 01 Exercicio 12 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

t = 'CALCULE PESO IDEAL'
print(f'{t:*^95}', end='\n\n')

a = float(input('Informe a altura em metros(m): '))

p = (a*72.7)-58

print(f'\nSeu peso ideal é de {p}')
