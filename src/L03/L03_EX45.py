# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 45 Python Brasil (J.Siqueira 03/21)."""

# Desenvolver um programa para verificar a nota do aluno em uma prova com 
# 10 questões, o programa deve perguntar ao aluno a resposta de cada questão
# e ao final comparar com o gabarito da prova e assim calcular o total de 
# acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno
# utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar 
# o sistema. Após todos os alunos terem respondido informar:

# a. maior e menor acerto;

# b. total de alunos que utilizaram o sistema;

# c. média das notas da turma.

# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

import os
os.system('clear')

gabarito = {
                    1: 'A',
                    2: 'B',
                    3: 'C',
                    4: 'D',
                    5: 'E',
                    6: 'E',
                    7: 'D',
                    8: 'C',
                    9: 'B',
                    10:'A',
                }

questoes = len(gabarito.keys())
caderneta = {}
aluno = []
aluno_resposta = []
aluno_total = 0
acertos = 0 
acertos_total = 0
acertos_maior = 0
acertos_menor = 10
turma_acertos_maior = []
turma_acertos_menor = []
turma_media = 0
c = 80

while True:
    
    os.system('clear')
    print ('='*c)
    print ('PROVA SEMESTRAL'.center(c))
    print ('='*c)
    nome_aluno = input (f'Digite o nome do aluno [\033[1;32m{aluno_total}\033[1;m]: ' )
    print ('-'*c)
    aluno_total += 1
    nome_aluno = nome_aluno.upper()
    aluno.append(nome_aluno)

      
    for questao in gabarito:
        resposta = input (f'Questão [\033[1;33m{str(questao).zfill(2)}/{questoes}\033[1;m]: ')
        resposta = resposta.upper()
        aluno_resposta.append (resposta)
        if resposta == gabarito[questao]:
            acertos += 1
            acertos_total += 1
    print('\n')
        
    if acertos > acertos_maior:
        turma_acertos_maior = []
        acertos_maior = acertos
        turma_acertos_maior.append(acertos_maior)

    if acertos < acertos_menor:
        turma_acertos_menor = []
        acertos_menor = acertos
        turma_acertos_menor.append(acertos_menor)

    aluno.append (acertos)
    caderneta[nome_aluno] = aluno_resposta, acertos, (acertos/questoes)*100
    aluno_resposta = []
    acertos = 0 
    turma_media = acertos_total/aluno_total

    continua = input ('Deseja continuar [S/N]?: ')
    continua = continua.upper()
    if continua !='S':
        os.system('clear')
        break

print ('='*c)
print ('ESTÁTISTICAS DA PROVA'.center(c))
print ('='*c)
print (f'Total de alunos.........: {aluno_total}')
print (f'Acerto médio da turma...: {turma_media:.1f} acertos [{(acertos_total/(aluno_total*questoes))*100}%]')
print (f'Maior acertos na turma..: {turma_acertos_maior} acertos ')
print (f'Menor acertos na turma..: {turma_acertos_menor} acertos')
#print ('\n')
print ('='*c)
print ('RELAÇÃO ALUNOS QUE REALIZARAM A PROVA'.center(c))
print ('='*c)
c4 = '\033[1;34mALUNO\033[1;m'
c2 = '\033[1;34mACERTOS\033[1;m'
c1 = '\033[1;34mRESPOSTA\033[1;m'
print (f'{c1:68}{c2:27}{c4}')
for i in caderneta:
    print ('-'*c)
    v1 = caderneta[i]
    x1 = str(v1[1]).zfill(2).rjust(8)
    x2 = str(v1[2])
    x3 = ''
    print (f'{v1[0]}{x1} [{x2}%]{x3:5}{i}')
print ('\n')



# ================================================================================
#                              ESTÁTISTICAS DA PROVA                              
# ================================================================================
# Total de alunos.......: 4
# Média da turma........: 5.2
# Maior acertos na turma: [10] 
# Menor acertos na turma: [2] 
# ================================================================================
#                      RELAÇÃO ALUNOS QUE REALIZARAM A PROVA                      
# ================================================================================
# RESPOSTA                                                ACERTOS        ALUNO
# --------------------------------------------------------------------------------
# ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']      10 [100.0%]     JEFERSOM
# --------------------------------------------------------------------------------
# ['A', 'B', 'C', 'D', 'E', 'A', 'A', 'A', 'A', 'A']      06 [60.0%]     SONIA
# --------------------------------------------------------------------------------
# ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']      02 [20.0%]     JUCA
# --------------------------------------------------------------------------------
# ['E', 'D', 'E', 'D', 'A', 'E', 'D', 'A', 'E', 'D']      03 [30.0%]     MARIA