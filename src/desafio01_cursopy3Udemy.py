"""47. Desafio de contadores."""

# Saida:
# 0 9
# 1 8
# 2 7
# 3 6
# 4 5
# 5 4
# 6 3
# 7 2
# 8 1
# 9 0

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(len(lista)):
#     print(i, lista[-i])


# m, n = 0, 0


for p, m in enumerate(range(10, 1, -1)):
    print(p, m)
