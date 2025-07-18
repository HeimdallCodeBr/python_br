import os
os.system('clear')

# Crie um "jogo dos estados". 
# 
# Neste jogo, o jogador precisa responder o nome da capital de cada Estado do Brasil.
# 
# O jogo deve perguntar ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. 
# 
# Após cada pergunta, o usuário pode escolher parar o jogo ou continuar para a próxima pergunta.
# 
# Quando o usuário decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.


estados = {
    'Acre':'Rio Branco',
    'Alagoas':'Maceió',
    'Amapá':'Macapá',
    'Amazonas':'Manaus',
    'Bahia':'Salvador',
    'Ceará':'Fortaleza',
    'Espirito Santo':'Vitória',
    'Goiás':'Goiânia',
    'Maranhão':'São Luís',
    'Mato Grosso':'Cuiabá',
    'Mato Grosso do Sul':'Campo Grande',
    'Minas Gerais':'Belo Horizonte',
    'Pará':'Belém',
    'Paraíba':'João Pessoa',
    'Paraná':'Curitiba',
    'Pernambuco':'Recife',
    'Piauí':'Teresina',
    'Rio de Janeiro':'Rio de Janeiro',
    'Rio Grande do Norte':'Natal',
    'Rio Grande do Sul':'Porto Alegre',
    'Rondônia':'Porto Velho',
    'Roraima':'Boa Vista',
    'Santa Catarina':'Florianópolis',
    'São Paulo':'São Paulo',
    'Sergipe':'Aracaju',
    'Tocantins':'Palmas',
}



n = ''
continua = ''
digitados = []
tentativa = 0
tentativas = 3
t = len(estados)
erros = 0
acertos = 0
total = 0
percetual = 0

while True:
    digitados.append(n)
    n = int(input(f'\nDigite um numero entre 0 e {t}: '))
    if (n in digitados):
        print(f'numero {n} já foi digitado!, digite novamente: ')
    elif (n < 0 or n >= t):
        print(f'Valor digitado incorreto! você tem {tentativas-tentativa-1} tentativa(s)')
        tentativa += 1
        if tentativa >= tentativas:
            print('\n**********************')
            print('* * * GAME OVER! * * *')
            print('**********************\n')
            break
        
    
    for i, estado in enumerate(estados):
        if i == n:
            capital = input(f'Qual é a capital de {estado}? ')
            if capital == estados.get(estado):
                print('Acertou\n')
                acertos +=1
            else:
                print('Errou!\n')
                erros +=1
    
    continua = input('Deseja continuar? S/N: ')
    if continua in 'Nn' or continua =='':
        total = acertos+erros
        percentual = (acertos/total)*100
        print ('\n---------------------------------')
        print (f'Você respondeu total de {total} perguntas')
        print (f'{acertos} ACERTOS')
        print (f'{erros} ERROS')
        print (f'Aproveitamento de {percentual:.0f}%')
        print ('---------------------------------\n')
        break
