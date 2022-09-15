"""Resolução Lista 02 Exercicio 12 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios

# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
# descontos são do Imposto de Renda, que depende do salário bruto (conforme
# tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário
# Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá
# pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas
# no mês.

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
# dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a
# quantidade de hora é 220.

# Salário Bruto: (5 * 220) : R$ 1100,00
# (-) IR (5%)              : R$ 55,00
# (-) INSS ( 10%)          : R$ 110,00
# FGTS (11%)               : R$ 121,00
# Total de descontos       : R$ 165,00
# Salário Liquido          : R$ 935,00


hora_valor = float(input('Informe o valor por hora.................: '))
hora_trabalhadas = int(input('Informe a quantidade de horas trabalhadas: '))

salario_bruto = hora_valor * hora_trabalhadas

if salario_bruto > 900 and salario_bruto <= 1500:
    desconto_ir = 0.05
elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_ir = 0.10
elif salario_bruto > 2500:
    desconto_ir = 0.20

desconto_sindicato = 0.03
desconto_inss = 0.10
fgts = 0.11
desconto_total = (
    (salario_bruto * desconto_inss)
    + (salario_bruto * desconto_ir)
    + (salario_bruto * desconto_sindicato)
)
salario_liquido = salario_bruto - desconto_total


print(
    f'\nSalário Bruto ({hora_valor}R$/h*{hora_trabalhadas}h) \
{salario_bruto:>15.2f}R$'
)
print(
    f'    (-) IR {desconto_ir*100:.0f}% {salario_bruto * desconto_ir:>30.2f}R$'
)
print(f'    (-) INSS 10% {salario_bruto * desconto_inss:>27.2f}R$')
print(f'    (-) Sindicato 3% {salario_bruto * desconto_sindicato:>23.2f}R$')
print(f'FGTS 11% {salario_bruto * fgts:>35.2f}R$')
print(f'Total de descontos {desconto_total:>25.2f}R$')
print(f'Salário Liquido {salario_liquido:>28.2f}R$')
