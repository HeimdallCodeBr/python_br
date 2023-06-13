import pyodbc

conexao = (
    "Driver={MySQL ODBC 8.0 Unicode Driver};"
    "Server=172.17.0.3;"
    "Database=Teste;"
    "UID=root;"
    "PWD=kAira#2012!;"
)


c = pyodbc.connect(conexao)
print("Conexão ok")
