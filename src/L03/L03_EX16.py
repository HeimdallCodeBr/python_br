# -*- coding: utf-8 -*-

"""Resolução Lista 3 Exercicio 16 Python Brasil (J.Siqueira 03/21)."""

# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,
# Faça um programa que gere a série até que o valor seja maior que 500.


# EXEMPLO: 
# n =	    0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	...
# f(n) =	0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	...

# https://www.mathsisfun.com/numbers/fibonacci-sequence.html


j = 0
i = 1

while True:
    t = i + j
    i = j
    j = t

    if i <= 2500:
        print(f"{i}", end=", ")
    else:
        break

print("\n")
