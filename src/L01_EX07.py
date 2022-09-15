"""Resolução Lista 01 Exercicio 07 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

t = 'CALCULO DA AREA DO QUADRADO'
print(f'{t:*^95}', end='\n\n')


s = int(input('Digite medida do quadrado em centimetros: '))
a = s**2
print(f'\nMedida digitada....: {s}cm')
print(f'Área...............: {a:.1f}cm²')
print(f'Dobro da área......: {2*a:.1f}cm²')
