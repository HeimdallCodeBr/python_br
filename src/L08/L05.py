# -*- coding: utf-8 -*-

import os

"""Resolução Lista 08 Exercicio 05 Python Brasil (J.Siqueira 02/23)."""

"""
5. Classe Conta Corrente:

Crie uma classe para implementar uma conta corrente.

A classe deve possuir os seguintes atributos:
- número da conta,
- nome do correntista,
- saldo,

Os métodos são os seguintes:
- alterarNome,
- depósito,
- saque,

No construtor,
saldo é opcional, com valor default zero e os demais
atributos são obrigatórios.

"""
os.system('clear')


class ContaCorrente():

    def __init__(self, numero_conta, nome_correntista):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = 0

    def AlterarNome(self, nome_correntista_novo):
        self.nome_correntista = nome_correntista_novo

    def Depositar(self, valor_deposito):
        self.saldo += valor_deposito

    def Saque(self, valor_saque):
        self.saldo -= valor_saque

    def MostraConta(self):
        return self.numero_conta, self.nome_correntista, self.saldo


c1 = ContaCorrente(56565, 'Jefersom')
c2 = ContaCorrente(55544, 'Marcia')
c3 = ContaCorrente(56432, 'Jose')

c1.Depositar(100)
c2.Saque(10)
c3.Depositar(600)

print(c1.MostraConta())
print(c2.MostraConta())
print(c3.MostraConta())

print('-------------------------')

c1.Saque(67)
c2.Depositar(100)
c3.Saque(890)
c1.AlterarNome('Juca')

print(c1.MostraConta())
print(c2.MostraConta())
print(c3.MostraConta())

print('-------------------------')
c1.Depositar(89)
c1.Saque(10)
c2.Depositar(1000)
c3.Depositar(899)
c2.Saque(450)
c3.Saque(890)
c1.Saque(112)

print(c1.MostraConta())
print(c2.MostraConta())
print(c3.MostraConta())
