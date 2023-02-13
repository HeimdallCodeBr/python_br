"""Resolução Lista 01 Exercicio 14 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

t = 'CALCUL PESO IDEAL'
print(f'{t:*^95}', end='\n\n')

p = float(input('Informe a quantidade de peixes pescados em kg...:'))

if p > 50:
    e = p-50
    m = e * 4
    print(f'\nTotal pescado..............: {p}kg')
    print(f'Excedente..................: {e:.1f}kg')
    print(f'Valor da multa a ser paga..: {m:.2f}R$')
else:
    print('\nTotal pescado dentro limite permitido')
