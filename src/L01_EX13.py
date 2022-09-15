"""Resolução Lista 01 Exercicio 13 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

t = 'CALCULE PESO IDEAL'
print(f'{t:*^95}', end='\n\n')

h = float(input('Informe sua altura.................: '))
s = input('Informe o sexo [M]asculino ou [F]eminino.: ')


if s.lower() == 'm':
    print(f'Peso ideal {(72.7*h)-58:.1f}')
elif s.lower() == 'f':
    print(f'Peso ideal {(62.1*h)-44.7:.1f}')
else:
    print('Valor digitado é inválido')
