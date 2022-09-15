# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 44 Python Brasil (J.Siqueira 03/21)."""

# Em uma eleição presidencial existem quatro candidatos. Os votos são
# informados por meio de código. Os códigos utilizados são:

# 1 , 2, 3, 4 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco

# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos.
# Para finalizar o conjunto de votos tem-se o valor zero.

import os
os.system('clear')

f = 47
i = 0
p = 0
Lista_candidatos = ['-', 'José', 'Maria', 'João', 'Pedro', 'NULO', 'BRANCO' ]
Lista_voto = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

while True:
    print('*'*f)
    print('VOTO ELETRONICO')
    print('*'*f)
    print(f'Candidato [{Lista_candidatos[1]}]\tdigite [1]')
    print('-'*f)
    print(f'Candidato [{Lista_candidatos[2]}]\tdigite [2]')
    print('-'*f)
    print(f'Candidato [{Lista_candidatos[3]}]\tdigite [3]')
    print('-'*f)
    print(f'Candidato [{Lista_candidatos[4]}]\tdigite [4]')
    print('-'*f)
    print(f'Voto [{Lista_candidatos[5]}]\t\tdigite [5]')
    print('-'*f)
    print(f'Voto [{Lista_candidatos[6]}]\t\tdigite [6]')
    print('-'*f)
    print(f'Total de votos computados \033[1;32m{i}\033[1;m')
    
    voto = int(input('\nDigite o voto para candidato: '))
    if voto == 0:
        break
    else:
        if voto in (1,2,3,4,5,6):
            Lista_voto[voto] += 1
            os.system('clear')
        else:
            input('\033[1;31mErro! digite novamente...\033[1;m')
            i -= 1
            os.system('clear')
    i += 1

    

os.system('clear')
print('*'*f)
print('RESULTADO DA VOTAÇÃO')
print('*'*f)
print(f'Total de votos computados:     \033[1;32m{i}\033[1;m')
print('-'*f)

for k in Lista_voto:
    p = (Lista_voto[k]/i)*100
    if Lista_voto[k] == 0:
        print(f'[{k}] Candidato {Lista_candidatos[k]}\tVotos: \033[1;31m{Lista_voto[k]}\033[1;m\t{p:.1f}% ')
    else:
        print(f'[{k}] Candidato {Lista_candidatos[k]}\tVotos: \033[1;33m{Lista_voto[k]}\033[1;m\t{p:.1f}% ')
    print('-'*f)
print('\n')



# ***********************************************
# VOTO ELETRONICO
# ***********************************************
# Candidato [José]        digite [1]
# -----------------------------------------------
# Candidato [Maria]       digite [2]
# -----------------------------------------------
# Candidato [João]        digite [3]
# -----------------------------------------------
# Candidato [Pedro]       digite [4]
# -----------------------------------------------
# Voto [NULO]             digite [5]
# -----------------------------------------------
# Voto [BRANCO]           digite [6]
# -----------------------------------------------
# Total de votos computados 11

# Digite o voto para candidato: 0




# ***********************************************
# RESULTADO DA VOTAÇÃO
# ***********************************************
# Total de votos computados:     11
# -----------------------------------------------
# [1] Candidato José      Votos: 1        9.1% 
# -----------------------------------------------
# [2] Candidato Maria     Votos: 3        27.3% 
# -----------------------------------------------
# [3] Candidato João      Votos: 2        18.2% 
# -----------------------------------------------
# [4] Candidato Pedro     Votos: 2        18.2% 
# -----------------------------------------------
# [5] Candidato NULO      Votos: 2        18.2% 
# -----------------------------------------------
# [6] Candidato BRANCO    Votos: 1        9.1% 
# -----------------------------------------------

