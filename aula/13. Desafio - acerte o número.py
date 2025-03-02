# * * * * * * * * * * * * * * *
# Elaborado por: JMS 25/11/2024
# * * * * * * * * * * * * * * *

# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

numero = 10

valor = int(input('Digite um numero secreto[1]: '))
if valor != numero:
    if valor < numero:
        print('o numero é maior ')
    if valor > numero:
        print('o numero é menor')
    valor = int(input('Digite um numero secreto[2]: '))
    if valor != numero:
        if valor < numero:
            print('o numero é maior ')
        if valor > numero:
            print('o numero é menor')
        valor = int(input('Digite um numero secreto[3]: '))
        if valor != numero:
            print('GAME OVER!')
        else:
            print('ACERTOU!')
    else:
        print('ACERTOU!')
else:
    print('ACERTOU!')




