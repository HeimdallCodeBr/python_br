# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 48 Python Brasil (J.Siqueira 04/22)."""

# Faça um programa que peça um numero inteiro positivo e em seguida 
# mostre este numero invertido.

# Exemplo:

#   12376489 
#   => 98467321

import os
os.system('clear')
n = ''
c = 40

print ('='*c)
print ('INVERTE NUMEROS')
print ('='*c)



while True:
    
    numero = input('Digite numero inteiro positivo: ')
    n += numero   

    if numero == '':
        break
    
    

print (f'\n{n}')
print (f'=> {n[::-1]}')


# ========================================
# INVERTE NUMEROS
# ========================================
# Digite numero inteiro positivo: 1
# Digite numero inteiro positivo: 2
# Digite numero inteiro positivo: 3
# Digite numero inteiro positivo: 4
# Digite numero inteiro positivo: 5
# Digite numero inteiro positivo: 6
# Digite numero inteiro positivo: 7
# Digite numero inteiro positivo: 8
# Digite numero inteiro positivo: 9
# Digite numero inteiro positivo: 

# 123456789
# => 987654321