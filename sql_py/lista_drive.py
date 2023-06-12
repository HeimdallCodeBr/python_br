import pyodbc

lista = pyodbc.drivers()
for li in lista:
    print(li)
