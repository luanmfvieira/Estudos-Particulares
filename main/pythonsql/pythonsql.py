import pyodbc

dados_conexao = (
    "Driver={MySQL ODBC 9.4 Unicode Driver};"
    "Server=127.0.0.1;"
    "Database=pythonsql;"
     "User=root;"           # seu usuário
    "Password=@Aguamineral10;"
    "Port=3306;"
)

conexao = pyodbc.connect(dados_conexao)
print("conexão realizada com sucesso!")

cursor = conexao.cursor()

cliente = "Fernanda"
produto = "Carregador"
data_venda = "2025-08-14"
preco = "90"
quantidade = 2

comando = f"""update vendas set id_venda = '3' where id_venda = '4';"""

cursor.execute(comando)
cursor.commit()

