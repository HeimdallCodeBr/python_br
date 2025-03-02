# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

nome = input('Digite um nome: ')
idade = input('Digite sua idade: ')
nova_idade = str(int(idade)+5)
total_letras = str(len(nome))

print('Olá ' + nome)
print('Total de letras do seu nome é ' + total_letras)
print('Daqui a 5 anos você tera ' + nova_idade)
