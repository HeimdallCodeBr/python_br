"""Resolução Lista 02 Exercicio 15 Python Brasil (J.Siqueira 03/21)."""

# https://wiki.python.org.br/ListaDeExercicios


# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
# informar se os valores podem ser um triângulo. Indique, caso os lados formem
# um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for
# maior que o terceiro;

# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

a = float(input("Digite medida a: "))
b = float(input("Digite medida b: "))
c = float(input("Digite medida c: "))

if a == b == c:
    print("\nTriângulo Equilátero")
elif a == b != c or a != b == c or a == c:
    print("\nTriângulo Isósceles")
else:
    print("\nTriângulo Escaleno")
