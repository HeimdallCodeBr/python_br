"""Resolução Lista 02 Exercicio 03 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
# letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

v = input('Digite sexo da pessoa...: ')

if v in 'Ff':
    print('Sexo Feminino')
elif v in 'Mm':
    print('Sexo Masculino')
else:
    print('Valor Inválido')
