# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

palavras = ['banana', 'maça', 'abacaxi', 'perâ', 'mamão']
tamanho = 0

for palavra in palavras:
    if len(palavra) >= 5:
        print(palavra)
