# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !

numeros = [45, 60, 10, 34, 98, 81, 11, 42, 46]
maior = 0
for numero in numeros:
    if numero > maior:
        maior = numero

print (f'Sequencia dada:  {numeros}')
print (f'O maior numero da sequencia é {maior}')

