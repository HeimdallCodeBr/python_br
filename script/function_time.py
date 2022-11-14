import os
import time

os.system('clear')

# Método time retorna segundos apartir do EPOCH (marco zero) 01/01/1970

s = time.time()
print(s)

# Retorna data e hora no formato americano
tempo = time.ctime()
print(tempo)

# Retorna o tempo formato de data
ano = time.gmtime().tm_year
mes = time.gmtime().tm_mon
dia = time.gmtime().tm_mday
dia_semana = time.gmtime().tm_wday
dia_ano = time.gmtime().tm_yday


print(dia, mes, ano)
print(dia_semana)
print(dia_semana)
print(dia_ano)
