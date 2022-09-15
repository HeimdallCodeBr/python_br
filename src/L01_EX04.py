"""Resolução Lista 01 Exercicio 04 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

t = 'MÉDIA BIMESTRAL - 2020'
print(f'{t:*^50}', end='\n\n')

n1 = int(input('Digite nota 1: '))
n2 = int(input('Digite nota 2: '))
n3 = int(input('Digite nota 3: '))
n4 = int(input('Digite nota 4: '))

print(f'\nA média das notas: {n1}, {n2}, {n3}, {n4} é {(n1+n2+n3+n4)/4}')
