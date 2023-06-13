# ---------------------------------------
# Lista drives ODBC instalados no sistema
# ---------------------------------------

import pyodbc

lista = pyodbc.drivers()
for li in lista:
    print(li)
