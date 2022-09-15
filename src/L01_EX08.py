"""Resolução Lista 01 Exercicio 08 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

t = 'CALCULAR HORAS TRABALHADAS MENSAL'
print(f'{t:*^95}', end='\n\n')


h = int(input('Digite total de horas trabalhadas no mês: '))
v = float(input('Digite o valor R$ por hora..............: '))

print(f'\nTotal de horas trabalhadas no mês....: {h}h')
print(f'Valor da hora........................: {v:.2f}R$')
print(f'Total a ser pago.....................: {v*h:.1f}R$/mês')
