# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !

numeros = [1, 2, 3, 4, 5]
soma = 0
i = 0

for numero in numeros:
    soma = soma + numero
    i += 1

print (f'A soma da sequencia é de {soma}')
print (f'A média da sequencia é de {soma/i}')
