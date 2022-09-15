"""Resolução Lista 02 Exercicio 11 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios

# As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contraram para desenvolver o programa que calculará
# os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo
# o seguinte critério, baseado no salário atual:

#   * salários até R$ 280,00 (incluindo) : aumento de 20%
#   * salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#   * salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#   * salários de R$ 1500,00 em diante :
#     aumento de 5% Após o aumento ser realizado, informe na tela:
#           o salário antes do reajuste;
#           o percentual de aumento aplicado;
#           o valor do aumento;
#           o novo salário, após o aumento.


salario = int(input('Informe o salario do colaborador: '))
salario_reajustado = 0


if salario <= 280:
    salario_reajustado = salario * 1.20
    reajuste = 20
elif salario > 280 and salario <= 700:
    salario_reajustado = salario * 1.15
    reajuste = 15
elif salario > 700 and salario <= 1500:
    salario_reajustado = salario * 1.10
    reajuste = 10
elif salario > 1500:
    salario_reajustado = salario * 1.05
    reajuste = 5

aumento = salario_reajustado - salario

print(f'Salario atual.........: {salario:.2f}R$')
print(f'Reajuste..............: {reajuste:.0f}%')
print(f'Aumento...............: {aumento:.2f}R$%')
print(f'Salario reajustado....: {salario_reajustado:.2f}R$')
