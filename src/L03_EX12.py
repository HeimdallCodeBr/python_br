# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 12 Python Brasil (J.Siqueira 03/21)."""

# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
# número inteiro entre 1 a 10. O usuário deve informar de qual numero ele
# deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50


t = int(input("Informe a tabuada a ser gerada: "))
print(f"\n* * * * * TABUADA DO {t} * * * * *")

for i in range(1, 11):
    print(f"{t} x {i} = {t * i}")
