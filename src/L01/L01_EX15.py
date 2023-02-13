"""Resolução Lista 01 Exercicio 15 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

t = 'CALCULO PESO IDEAL'
print(f'{t:*^30}', end='\n\n')

hv = float(input('Informe o valor de horas/R$..................: '))
ht = float(input('Informe o total de horas trabalhadas no mês..: '))

sb = hv * ht
ir = sb * (11 / 100)
inss = sb * (8 / 100)
sind = sb * (5 / 100)
sl = sb - (ir + inss + sind)

print(f'\n+ Salário Bruto....{sb:.>10.2f} R$')
print(f'  - IR (11%).......{ir:.>10.2f} R$')
print(f'  - INSS (8%)......{inss:.>10.2f} R$')
print(f'  - Sindicato (5%).{sind:.>10.2f} R$')
print(f'= Salário Liquido..{sl:.>10.2f} R$')
