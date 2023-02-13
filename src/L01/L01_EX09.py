"""Resolução Lista 01 Exercicio 09 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

t = 'CONVERTER TEMPERATURA DE FAHRENHEIT'
print(f'{t:*^95}', end='\n\n')

# C = 5 * ((F-32) / 9) FORMULA PARA CONVERTER DE F-->C

f = float(input('Digite o valor da temperatura em ᵒF..: '))

c = ((f-32)/9)
print(f'\nTemperatura digitada, {f:.1f}ᵒF, seu valor em Celsius é {c:.1f}ᵒC')
