# Dado duas listas, printe todos os valores que aparecerem
# duplicados nas duas listas.


lista1 = [12, 24, 67, 45]
lista2 = [34, 12, 34, 11, 90]

for l1 in lista1:
    for l2 in lista2:
        if l1 == l2:
            print(f'o numero {l1} contem nas duas listas')

