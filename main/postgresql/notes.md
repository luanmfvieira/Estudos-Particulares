#gerenciador de banco de dados, suporta alto volumes, funcional em site com acessos simultaneos

- Open source, utilização gratuita

- Extensões, trabalhar com outros tipos de dados e linguagem, como python

- SGBD (Sistema de gerenciamento de banco de dados), postgresql é um dos 4 maiores, dentre eles existem oracle, mysql e sql server

comandos

CREATE DATABASE nomedoarquivo;  #criar
DROP DATABASE nomedoarquivo;    #deletar



-----------------------------------------------------------------------------------------------

SERIAL, NOT NULL, UNIQUE, INT, CREATE TABLE, ID SERIAL PRIMARY KEY, VARCHAR

/*

Para criar uma coluna, e o nome é usuarios

SERIAL significa que ele cadastra direto o por numero, usuario 1, 2 e etc

NOT NULL é para garantir que o campo não pode ser nulo

UNIQUE é para garantir que exista apenas um dele na tabela

idade INT para informar que será recebido um número inteiro

/* E */ para abrir e fechar anotações particulares que não interferiram na run do code

*/

CREATE TABLE usuarios (   
	id SERIAL PRIMARY KEY, 
	nome VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
	idade INT,
	data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	

);

-----------------------------------------------------------------------------------------------

/*

INSERT INTO é para inserir dados na tabela
VALUES seriam os valores que você quer inserir
(não é obrigatório colocar as colunas nas quais você quer inserir, digitar (nome, email, idade, parece que o proprio sistema ja vai colocando de 1 em 1))

*/



INSERT INTO usuarios (nome, email, idade)
VALUES ('João', 'joao@gmail.com', 26);


-----------------------------------------------------------------------------------------------

SELECT * FROM usuarios;  (usuarios foi a tabela escolhida e * para ver tudo, mostra o que foi feito)


-----------------------------------------------------------------------------------------------


/*

ponto e virgula no final sempre

*/



INSERT INTO usuarios (nome, email, idade)
VALUES

('João', 'joao@gmail.com', 26),
('Ana', 'ana@gmail.com', 23),
('Luan', 'luan@gmail.com', 25),
('Renata', 'renata@gmail.com', 28),
('Alberta', 'alberta@gmail.com', 23);



-----------------------------------------------------------------------------------------------


UPDATE usuarios SET idade = 50 WHERE nome = 'João'

alterei a idade do joão para 50



-----------------------------------------------------------------------------------------------

DELETE FROM usuario WHERE nome = 'João';

deletei a coluna João

-----------------------------------------------------------------------------------------------

CREATE TABLE pedidos (
	id SERIAL PRIMARY KEY,                               #id serial primary key é para o que for criado ter o id 1, 2, 3 etc
	usuario_id INT REFERENCES usuarios(id),              #para que vincule os usuarios da table usuarios com a mesma de pedidos
	valor DECIMAL(10,2),
	data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

criei a table pedidos



-----------------------------------------------------------------------------------------------


INSERT INTO pedidos(usuario_id, valor)
VALUES
(4, 10.00)


coloquei o valor 10 ao usuario 4 


-----------------------------------------------------------------------------------------------

SELECT u.nome, p.valor
FROM usuarios u
JOIN pedidos p ON u.id = p.usuario_id;



isso é para juntar pedidos com p, u.id recebe pedidos usuarios id então junta

usuario.nome, pedidos.valor

u.nome #nome, da tabela usuarios

p.valor # o valor, da tabela pedidos

FROM usuarios u #trazer como base usuarios

-----------------------------------------------------------------------------------------------

SELECT AVG(idade) AS idade_media FROM usuarios;

para pegar a media de idade dos usuarios

-----------------------------------------------------------------------------------------------


CREATE TABLE produtos(
	id SERIAL PRIMARY KEY,
	dados JSONB
);

INSERT INTO produtos (dados)
VALUES
('{"nome": "Celular", "preco":3000}');


inseri a tabela produtos e nela o nome, que recebe celular e o preço que recebe 3000, tudo no mesmo id

-----------------------------------------------------------------------------------------------




SELECT dados->>'nome' AS nome_produto FROM produtos;

para trazer apenas o nome do produto

-----------------------------------------------------------------------------------------------
nome VARCHAR(100)

para ser variavel em caracteres, até 100 carac


-----------------------------------------------------------------------------------------------
CREATE TABLE categorias (
	ID SERIAL PRIMARY KEY,
	nome VARCHAR(100),
	tags TEXT[]
	
);

INSERT INTO categorias(nome, tags)
VALUES
('Eletrônicos', ARRAY['tecnologia', 'gadgets'])

#ARRAY PARECE SER O COMANDO PARA COLOCAR AS COISAS NA LISTA TEXT[]




-----------------------------------------------------------------------------------------------
create index idx_none on usuarios (nome);

criar um index na table usuarios em nome



para analisar a consulta digite

explain analyze select * from usuarios where nome = 'João';

-----------------------------------------------------------------------------------------------
























