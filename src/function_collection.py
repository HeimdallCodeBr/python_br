from collections import Counter
from os import system

system('clear')

vendas_tecnologia = {'notebook asus': 2450,
                     'iphone': 15000,
                     'samsung galaxy': 12000,
                     'tv samsung': 10000,
                     'ps5': 14300,
                     'tablet': 1720,
                     'notebook dell': 17000,
                     'ipad': 1000,
                     'tv philco': 2500,
                     'notebook hp': 1000
                     }


m = Counter(vendas_tecnologia).most_common(5)
print(m)


print('\n')
