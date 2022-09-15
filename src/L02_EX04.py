"""Resolução Lista 02 Exercicio 04 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios

# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

s = input('Digite uma letra...: ')

if s.lower() in 'aeiou':
    print('vogal')
else:
    print('consoante')
