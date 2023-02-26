# -*- coding: utf-8 -*-

"""Resolução Lista 05 Exercicio 07 Python Brasil (J.Siqueira 02/23)."""

"""
7. Faça um programa que use a função valorPagamento para determinar o
valor a ser pago por uma prestação de uma conta.

O programa deverá solicitar ao usuário o valor da prestação e o número
de dias em atraso e passar estes valores para a função valor Pagamento,
que calculará o valor a ser pago e devolverá este valor ao programa que
a chamou.

O programa deverá então exibir o valor a ser pago na tela.

Após a execução o programa deverá voltar a pedir outro valor de prestação e
assim continuar até que seja informado um valor igual a zero para a
prestação.

Neste momento o programa deverá ser encerrado, exibindo o relatório do dia,
que conterá a quantidade e o valor total de prestações pagas no dia.

O cálculo do valor a ser pago é feito da seguinte forma.

Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver
atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

"""


def valorPagamento(valor_aluguel: float, dias_atraso: int) -> float:
    '''
    valorPagamento:
                Calcula a multa devido ao atrado do
                pagamento do aluguel

    Parametros:
                valor_aluguel(float): valor do aluguel
                dias_atraso(int): dias em atraso
    Retorna:
                (float): retorna a valor parcela corrigido,
                multa 3% + 0,1% de juros por dia atraso.

    '''
    multa = 0.03   # 3%  multa por atraso
    juros_dia = 0.001  # 0.1 juros por dia
    valor_aluguel += valor_aluguel * multa + \
        ((valor_aluguel * juros_dia) * dias_atraso)

    return valor_aluguel


# ==================
# PROGRAMA PRINCIPAL
# ==================

relatorio_dia = 0.0
parcelas_pagas = 0

while True:
    aluguel = float(input('Informe o  valor do aluguel: '))
    if aluguel == 0:
        break
    atraso = int(input('Informe os dias em atraso: '))
    print(valorPagamento(aluguel, atraso))
    parcelas_pagas += 1
    relatorio_dia += valorPagamento(aluguel, atraso)

print(
    f'\nForam pagos {parcelas_pagas} alugueis, totalizando R${relatorio_dia:.2f}')
