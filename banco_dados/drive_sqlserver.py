import pymssql

conn2 = pymssql.connect(
    server="sqlserver2022",
    user="SA",
    password="kAira#2012!",
    database="TestDB",
    port=1433,
)


print("conectado com sucesso!")
