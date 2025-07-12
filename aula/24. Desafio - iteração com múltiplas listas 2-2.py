# Dado duas listas, printe uma mensagem dizendo se existe
# algum elemento em comum entre elas ou não.

lista1 = [10.0, 10.0, 45]
lista2 = [10.0, 12.5, 'xxxx', False, 'xxxx']
elemento = False
c = 0

for l1 in lista1:
    if elemento:
        break
    for l2 in lista2:
        c += 1
        if l1 == l2:
            elemento = True
            break

if elemento:
    print(f'Listas contem elementos em comum, INTERAÇÔES TOTAIS {c}')
else:
    print(f'Lista NÃO contem elementos em comum, INTERAÇÔES TOTAIS {c}')