"""Resolução Lista 01 Exercicio 18 Python Brasil (J.Siqueira 08/20)."""

# https://wiki.python.org.br/ListaDeExercicios

# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input('Informe o tamanho do arquivo em MB.....: '))
velocidade = float(input('Informe a velocidade da conexão em Mbps: '))

tempo = (arquivo / velocidade) / 60

print(f'Tempo aproximado de download {tempo:.1f} minutos')
