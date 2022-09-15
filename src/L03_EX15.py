# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 15 Python Brasil (J.Siqueira 03/21)."""

# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,
# ... Faça um programa capaz de gerar a série até o n−ésimo termo.

# EXEMPLO: 
# n =	    0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	...
# f(n) =	0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	...

# https://www.mathsisfun.com/numbers/fibonacci-sequence.html



n = int(input("\nInforme numero para gerar a sequencia de Fibonacci: "))
a = 0
s = 1

for k in range(n + 1):
    t = s + a
    s = a
    a = t
    print(f'[{k}]:{s}', end=", ")
print("\n")
