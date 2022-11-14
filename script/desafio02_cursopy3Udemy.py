"""Validação dos dois ultimos digitos do CPF."""

# Exemplo: 168.995.350-09

# Algoritimo para descobrir penultimo digito:

# 1 * 10 = 10
# 6 * 9  = 54
# 8 * 8  = 64
# 9 * 7  = 63
# 9 * 6  = 54
# 5 * 5  = 25
# 3 * 4  = 12
# 5 * 3  = 15
# 0 * 2  = 0

# somatoria = 297

# Calculo: 11 - (297 % 11) = 11

# se 11 > 9 então penultimo digito do CPF vai ser 0

# ===============================================================

# Algoritimo para descobrir o ultimo digito:

# 1 * 11 = 10
# 6 * 10 = 54
# 8 * 9  = 64
# 9 * 8  = 63
# 9 * 7  = 54
# 5 * 6  = 25
# 3 * 5  = 12
# 5 * 4  = 15
# 0 * 3  = 0
# 0 * 2  = 0

# somatoria = 343

# Calculo: 11 - (343 % 11) = 9

# então o ultimo digito do CPF vai ser 9
