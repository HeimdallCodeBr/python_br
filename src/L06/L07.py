# -*- coding: utf-8 -*-

"""Resolução Lista 06 Exercicio 07 Python Brasil (J.Siqueira 02/23)."""

"""
Conta espaços e vogais.

Dado uma string com uma frase informada pelo
usuário (incluindo espaços em branco), conte:

a. quantos espaços em branco existem na frase.

b. quantas vezes aparecem as vogais a, e, i, o, u.

"""

caminho = '/home/jefersom/Projetos/python_br/src/L06/'

with open(fr'{caminho}biblia-em-txt.txt', 'r') as arquivo:
    texto = arquivo.read()


espaco = 0
vogais = 0
consoantes = 0

for t in texto:
    if t == ' ':
        espaco += 1
    if t in ('aeiou'):
        vogais += 1
    if t not in ('aeiou. '):
        consoantes += 1

print(f'Total de {espaco:,.0f} espaços em branco')
print(f'Total de {vogais:,.0f} vogais')
print(f'Total de {consoantes:,.0f} consoantes')
