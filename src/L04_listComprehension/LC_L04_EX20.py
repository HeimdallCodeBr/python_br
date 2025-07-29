# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 20 Python Brasil (J.Siqueira 04/22)."""

# As Organizações Tabajara resolveram dar um abono aos seus colaboradores
# em reconhecimento ao bom resultado alcançado durante o ano que passou.
# Para isto contratou você para desenvolver a aplicação que servirá como
# uma projeção de quanto será gasto com o pagamento deste abono. Após
# reuniões envolvendo a diretoria executiva, a diretoria financeira e os
# representantes do sindicato laboral, chegou-se a seguinte forma de
# cálculo:

# Cada funcionário receberá o equivalente a 20% do seu salário bruto
# de dezembro; O piso do abono será de 100 reais, isto é, aqueles
# funcionários cujo salário for muito baixo, recebem este valor mínimo;

# Neste momento, não se deve ter nenhuma preocupação com colaboradores
# com tempo menor de casa, descontos, impostos ou outras particularidades.

# Seu programa deverá permitir a digitação do salário de um número
# indefinido (desconhecido) de salários.

# Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada
# de todos os dados o programa deverá calcular o valor do abono concedido
# a cada colaborador, de acordo com a regra definida acima. Ao final, o
# programa deverá apresentar:

# O salário de cada funcionário, juntamente com o valor do abono;
# O número total de funcionário processados;
# O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais;
# O maior valor pago como abono; A tela abaixo é um exemplo de execução do
# programa, apenas para fins ilustrativos.
# Os valores podem mudar a cada execução do programa.

# Projeção de Gastos com Abono
# ============================
# Salário: 1000
# Salário: 300
# Salário: 500
# Salário: 100
# Salário: 4500
# Salário: 0

# Salário         Abono
# R$ 1000.00  -   R$ 200.00
# R$ 300.00   -   R$ 100.00
# R$ 500.00   -   R$ 100.00
# R$ 100.00   -   R$ 100.00
# R$ 4500.00  -   R$ 900.00


# Foram processados 5 colaboradores
# Total gasto com abonos: R$ 1400.00
# Valor mínimo pago a 3 colaboradores
# Maior valor de abono pago: R$ 900.00

from os import system

system('clear')

salarios: list = []
c: int = 0
menor: int = 0
maior: int = 0
maior_valor: float = 0.0
abono: float = 0.0
abono_total: float = 0.0


while True:
    system('clear')
    print('Entrada {}'.format(c))
    print('================================')
    salario = input('Informe o valor do salário: ')

    if salario == '0':
        break
    else:
        if not str(salario).replace('.', '').isdigit():
            c -= 1
            print('não é numero')
            input()
        else:
            salario = float(salario)
            salarios.append(salario)

# ===================================
# HACK PARA GERAR NUMEROS ALEATORIOS
# ===================================
# z = 0
# sistema = []
# for i in range(2500):
#     a = randint(1, 3000)
#     b = randint(50, 5000)
#     z += 1
#     if a in sistema:
#         pass
#     else:
#         sistema.append(a)
#         salarios.append(b)
# ===================================


system('clear')
print('Projeção de Gastos com Abono')
print('============================')
print('Salário - Abono')

for s in salarios:

    abono = float(s) * 0.2
    c += 1
    if abono <= 100:
        abono = 100
        menor += 1
    else:
        maior += 1
        if abono >= maior_valor:
            maior_valor = abono

    abono_total += abono
    print('{:>7.2f} - {:>7.2f}'.format(float(s), abono))

print('\n')
print('Foram processados {} colaboradores'.format(c))
print('Total gasto com abonos: R$ {:.2f}'.format(abono_total))
print('Valor mínimo pago a {} colaboradores'.format(menor))
print('Maior valor de abono pago: R$ {:.2f}'.format(maior_valor))
