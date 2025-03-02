# * * * * * * * * * * * * * * *
# Elaborado por: JMS 23/11/2024
# * * * * * * * * * * * * * * *

# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
#   quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
#   variávies dentro do próprio código.


usuario = input('Informe o nome do usuário...: ') == 'admin'
senha = input('Informe a senha do usuário..: ') == '123'

print ('\n- - - - - INICIO - - - - -\n')
if usuario and senha:
    print('Acesso permitido!')
elif usuario != True:
    print('USUÁRIO incorreto!')
elif senha != True:
    print('SENHA incorreta!')
