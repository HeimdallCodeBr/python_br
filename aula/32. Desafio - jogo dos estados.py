import os
os.system('clear')

# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
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


print(estados["Tocantins"])


print('\n')