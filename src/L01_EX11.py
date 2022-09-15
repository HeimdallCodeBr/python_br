"""Resolução Lista 01 Exercicio 11 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

t = 'CALCULE'
print(f'{t:*^95}', end='\n\n')

n1 = int(input('Digite primeiro numero inteiro..: '))
n2 = int(input('Digite segundo numero inteiro...: '))
n3 = int(input('Digite terceiro numero natural..: '))

a = (n1*2)*(n2/2)
b = (n1*3)+n3
c = n3**3

print('\n')
print(f'O produto do dobro do primeiro com a metade do segundo é.: {a}')
print(f'A soma do triplo do primeiro com terceiro é..............: {b}')
print(f'O terceiro elevado ao cubo é.............................: {c}')
