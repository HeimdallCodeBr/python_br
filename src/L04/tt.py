from os import system
from random import randint

system('clear')

jogador = []
votos = []
x = 0
for i in range(1300):
    a = randint(1, 500)
    b = randint(100, 5000)
    x += 1
    if a in jogador:
        pass
    else:
        jogador.append(a)
        votos.append(b)

print(jogador)
print('\n')
print(votos)
