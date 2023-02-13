"""Resolução Lista 02 Exercicio 14 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios


# Faça um programa que lê as duas notas parciais obtidas por um aluno numa
# disciplina ao longo de um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo:

# Média de Aproveitamento        Conceito
# Entre 9.0 e 10.0               A
# Entre 7.5 e 9.0                B
# Entre 6.0 e 7.5                C
# Entre 4.0 e 6.0                D
# Entre 4.0 e zero               E

# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
# e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
# conceito for D ou E.

n1 = float(input('Informe a nota n1: '))
n2 = float(input('Informe a nota n2: '))

media = (n1 + n2) / 2

if media > 9 and media <= 10:
    conceito = 'A'
elif media > 7.5 and media <= 9:
    conceito = 'B'
elif media > 6 and media <= 7.5:
    conceito = 'C'
elif media > 4 and media <= 6:
    conceito = 'D'
elif media == 0 and media <= 4:
    conceito = 'E'
else:
    conceito = 'inválido'


if conceito in 'ABC':
    final = 'Aprovado'
else:
    final = 'Reprovado'


print(f'\nNota n1: {n1}')
print(f'Nota n2: {n2}')
print(f'Média: {media}\n')
print(f'Conceito: {conceito}')
print(f'Situação: {final}')
