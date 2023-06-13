import pyodbc
import pandas as pd
from os import system

system("clear")

dados_conexao = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=172.17.0.2, 1433;"
    "DATABASE=ContosoRetailDW;"
    "UID=SA;"
    "PWD=kAira#2012!;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão realizada!")

produtos = pd.read_sql("SELECT * FROM ContosoRetailDW.dbo.DimProduct", conexao)
print(produtos)
