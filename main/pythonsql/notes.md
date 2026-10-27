## comandos em mysql para criação do database primeiro


create database pythonsql

use pythonsql

create table Vendas
(
id_venda serial primary key,
cliente varchar(50),
produto varchar(50),
data_venda date,
preco decimal,
quantidade int
);



insert into vendas(cliente, produto, data_venda, preco, quantidade)
values
('Luan','PC','2025-08-22',8000,1);



(acabei criando duas iguais)

delete from vendas where id_venda = '2';


utilizar a biblioteca pyodbc

pip install pyodbc

baixei o mysql connector odbc 9.4.0 em

https://dev.mysql.com/downloads/file/?id=544576

consultei o meu servidor em cmd digitando hostname

(nome_do_servidor)

import pyodbc

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




(so funciona localmente, parece que preciso liberar o firewall caso queira conexões remotas

Criar o usuário no MySQL com permissão para qualquer host ou para o seu computador:

CREATE USER 'root'@'DESKTOP-KHCIRL3' IDENTIFIED BY '@Aguamineral10';
GRANT ALL PRIVILEGES ON pythonsql.* TO 'root'@'DESKTOP-KHCIRL3';
FLUSH PRIVILEGES;


Alterar bind-address no my.ini/my.cnf para 0.0.0.0 (permitir conexões externas).

Liberar a porta 3306 no firewall.)


comando cursor é o mesmo que query do sql na biblioteca


cursor = conexao.cursor()


comando = """insert into vendas(cliente, produto, data_venda, preco, quantidade)
values
('Renato','GPU','2025-08-20',5000,1);"""

cursor.execute(comando)
cursor.commit()      (você só usa o comando cursor.commit() caso faça alguma alteração no database)

retornou conexão realizada com sucesso!

cliente = "Fernanda"
produto = "Carregador"
data_venda = "2025-08-14"
preco = "90"
quantidade = 2

comando = f"""update vendas set id_venda = '3' where id_venda = '4';"""

cursor.execute(comando)
cursor.commit()






