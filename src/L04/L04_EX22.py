# -*- coding: utf-8 -*-

"""Resolução Lista 4 Exercicio 22 Python Brasil (J.Siqueira 04/22)."""

# Sua organização acaba de contratar um estagiário para trabalhar no Suporte
# de Informática, com a intenção de fazer um levantamento nas sucatas
# encontradas nesta área.
#
# A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram
# lá, testando e anotando o estado de cada um deles, para verificar o que se
# pode aproveitar deles. Foi requisitado que você desenvolva um programa para
# registrar este levantamento.
#
# O programa deverá receber um número indeterminado de entradas, cada uma
# contendo:
# um número de identificação do mouse
# o tipo de defeito:
# necessita da esfera;
# necessita de limpeza;
# necessita troca do cabo ou conector;
# quebrado ou inutilizado
#
# Uma identificação igual a zero encerra o programa. Ao final o
# programa deverá emitir o seguinte relatório:

# Quantidade de mouses: 100

# Situação                            Quantidade
# 1- necessita da esfera                  40
# 2- necessita de limpeza                 30
# 3- necessita troca do cabo ou conector  15
# 4- quebrado ou inutilizado              15


from os import system

system('clear')

defeito_nome: list = ['necessita da esfera',
                      'necessita de limpeza',
                      'necessita troca do cabo ou conector',
                      'quebrado ou inutilizado']

defeito_codigo: list = ['1', '2', '3', '4']

defeito_quantidade: list = [0] * len(defeito_codigo)

identificacao_mouse: list = []


while True:
    system('clear')
    print('======================================')
    for d, e in enumerate(defeito_codigo):
        print('{} - {}'.format(d, defeito_nome[int(d)]))
    print('Pressione 0 para sair ')
    print('======================================')
    print('\n')

    identificacao = input('A. Informe a identificação do mouse: ')
    if identificacao == '0':
        break
    else:
        if identificacao in identificacao_mouse:
            print('Já existe mouse com essa identificação')
            input()
        else:
            situacao = input('B. Informe a situação do equipamento: ')
            if not str(situacao).replace('.', '').isdigit():
                print('ERRO! valor digitado não é válido')
                input()
            else:
                if int(situacao) < 1 or int(situacao) > 4:
                    print('Digite valores entre 1 e 4')
                    input()
                else:
                    if situacao in defeito_codigo:
                        defeito_quantidade[defeito_codigo.index(situacao)] += 1
                        identificacao_mouse.append(identificacao)


print('\n')
print('Quantidade de mouses: {}'.format(sum(defeito_quantidade)))
print('\n')
print('{}\t{}'.format('Situação', 'Quantidade').expandtabs(42))
for a, w in enumerate(defeito_codigo):
    b = defeito_nome[int(a)]
    c = defeito_quantidade[int(a)]
    print('{} - {}\t{}'.format(a+1, b, c).expandtabs(23))
print('\n')
