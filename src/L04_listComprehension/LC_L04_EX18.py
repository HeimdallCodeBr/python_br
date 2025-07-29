# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 18 Python Brasil (J.Siqueira 04/22)."""

# Uma grande emissora de televisão quer fazer uma enquete entre os seus
# telespectadores para saber qual o melhor jogador após cada jogo. Para
# isto, faz-se necessário o desenvolvimento de um programa, que será
# utilizado pelas telefonistas, para a computação dos votos.
#
# Sua equipe foi contratada para desenvolver este programa, utilizando
# a linguagem de programação C++. Para computar cada voto, a telefonista
# digitará um número, entre 1 e 23, correspondente ao número da camisa do
# jogador.

# Um número de jogador igual zero, indica que a votação foi encerrada.
# Se um número inválido for digitado, o programa deve ignorá-lo, mostrando
# uma breve mensagem de aviso, e voltando a pedir outro número. Após o
# final da votação, o programa deverá exibir:

# a. O total de votos computados;
# b. Os númeos e respectivos votos de todos os jogadores que receberam votos;
# c. O percentual de votos de cada um destes jogadores;
# d. O número do jogador escolhido como o melhor jogador da partida,
# juntamente com o número de votos e o percentual de votos dados a ele.

# Observe que os votos inválidos e o zero final não devem ser computados como
# votos. O resultado aparece ordenado pelo número do jogador. O programa deve
# fazer uso de arrays. O programa deverá executar o cálculo do percentual de
# cada jogador através de uma função. Esta função receberá dois parâmetros: o
# número de votos de um jogador e o total de votos. A função calculará o
# percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo.
# O disposição das informações deve ser o mais próxima possível ao exemplo.
# Os dados são fictícios e podem mudar a cada execução do programa. Ao final,
# o programa deve ainda gravar os dados referentes ao resultado da votação em
# um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
#
# Enquete: Quem foi o melhor jogador?

# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50
# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0

# Resultado da votação:
# Foram computados 8 votos.
# Jogador Votos %
# 9         4       50,0%
# 10        3       37,5%
# 11        1       12,5%

# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total
# de votos.


from os import system
from random import randint

system('clear')

jogador: list = []
votos: list = []
resultado: list = []
vencedor: list = []
percentual = 0.0


while True:

    voto = input('Informe o numero do jogador: ')

    if voto == '0':
        break
    else:
        if voto.isdigit() and (int(voto) >= 1 and int(voto) <= 23):
            voto = int(voto)

            if voto in jogador:
                votos[jogador.index(voto)] += 1
            else:
                jogador.append(voto)
                votos.append(1)
        else:
            print('Informe um valor entre 1 e 23 ou 0 para sair!')


# x = 0
# for i in range(randint(50, 100)):
#     a = randint(1, 23)
#     b = randint(randint(0, 100), 100)
#     x += 1
#     if a in jogador:
#         pass
#     else:
#         jogador.append(a)
#         votos.append(b)


vencedor.append(jogador[votos.index(max(votos))])
vencedor.append(max(votos))
vencedor.append(round(max(votos)/sum(votos)*100, 3))

for j, k in enumerate(jogador):
    x = []
    x.append(jogador[j])
    x.append(votos[j])
    percentual = round((votos[j]/sum(votos))*100, 1)
    x.append(percentual)
    resultado.append(x)


print('\n')
print('Resultado da votação:')
print('Foram computados {} votos.'.format(sum(votos)))
print('Jogador  Votos  %')
resultado.sort()

for m, n in enumerate(resultado):
    r1 = str(resultado[m][0]).zfill(2)
    r2 = resultado[m][1]
    r3 = resultado[m][2]
    print('{}       {}     {}%'.format(r1, r2, r3))

print('\nO melhor jogador foi o número {}, com {} votos, correspondendo a {}% do total de votos.'.format(
    vencedor[0], vencedor[1], vencedor[2]))
