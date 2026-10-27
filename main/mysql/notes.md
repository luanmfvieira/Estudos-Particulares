SQL - STRUCTURED QUERY LANGUAGE  (linguagem de consulta estruturada)


os proprios frameworks de banco de dados provavelmente usam os comandos base de sql como select, into, delete, primary key etc

SGBD - SISTEMA DE GERENCIAMENTO DE BANCO DE DADOS

(DBMS - DATA BASE MANAGEMENT SYSTEM)

sql é diferente de IDE pois é apenas para gerenciar banco de dados


comando USE stackmobile;

para entrar na database stackmobile que você criou (stackmobile é um nome mas pode ser qualquer nome)

você precisa saber os comandos ao inves de usar a plataforma para caso você precise usar um terminal ao inves da propria IDE

drop database cadastro;  (comando drop database para excluir o database que quiser, prov da pra excluir table e etc)

--------------------------------------------------------------------------
# Tipos Primitivos

## 🔢 Inteiro
- `TinyInt` - 126bts
- `SmallInt`
- `Int` - 2bilhoes bts
- `MediumInt`
- `BigInt` para valores mto grandes

## 🔣 Real - numeros
- `Decimal`
- `Float`
- `Double`
- `Real`

## 🔘 Lógico
- `Bit`
- `Boolean`

## 🔠 Caractere
- `Char` - char ocupa todos os espaços que foram estabelecidos (exemplo char(30) dai voce digita luan e ele ocupa luan e todo o espaço restante até completar 30) (ocupa mais a memoria do sistema desnecessariamente e o arquivo fica maior)

- `VarChar` - especificar quantos caracteres você vai armazenar, exemplo VarChar(100)

## 📝 Texto
- `TinyText`
- `Text`
- `MediumText`
- `LongText`

## 📚 Coleção
- `Enum`
- `Set`

## 🕓 Data e Tempo
- `Date` dia / mes / ano
- `DateTime` a hora atual
- `Time`
-------------------------------------------


create table produto(
	id_produto int,
    nome varchar(30),
    preco double,  (valor fraccionado)
    descricao text  (text seria para textos muito grandes)
);

- em cima seria assim

    variavel tipo da variavel

    --------------------------------------

    comando desc para ver o que tem na tabela de forma detalhada

desc produto;

select * from produto;

------------------------------

insert into produto
(id_produto, nome, preco, descricao)
values
('1', 'RTX 4090', '2500.99', 'Placa topo de linha da Nvidia')

-------------------------------------------------------------

insert into produto
(id_produto, nome, preco, descricao)
values
('2','Core i5 12400F','970.75','Processador intel da 12th'),
('3','SSD 480GB','350.00','SSD da marca Smart Brasil');


-------------------------------------------------------------
(apos deletar tudo criei novamente dessa forma)


create table produto(
id_produto int not null auto_increment,       #not null para ser obrigatorio digitar algo
nome varchar(30) not null,                    #auto_increment para colocar o id automaticamente  e primary key para dar prioridade a essa chave
preco double not null,
descrica text not null,
primary key(id_produto)
);

----------------------------------------------------------------------------------

o ponto e vírgula (;) é utilizado para todo final de código, então sem ele voce consegue executar um código só, mas se for mais de um precisa por ; no final de cada codigo

-------------------------------------------------------------

select * from produto where id_produto = '1';

para consultar somente o id 1 da tabela


select * from produto where id_produto = '1' and nome = 'RTX 5080';  (para pegar por id e nome)

-----------------------------------------------------------------

update produto set nome = 'HD 1T' where id_produto = '5';

para atualizar o nome para hd 1t no id 5

-----------------------------------------------------------------



deletar a tabela 5 

delete from produto where id_produto = '5';



alter table produto
add column codigo int not null;      adicionou a coluna codigo


---------------------------------------------------


update produto set codigo = '500' where id_produto = '1';



para excluir uma coluna é 

alter table produto
drop column descrica;

tenha sempre um backup do seu banco de dados!!!

comando truncate produto;

exclui tudo o que estiver dentro da tabela produto

drop table produto;  exclui a tabela produto

drop database stackmobile;  exclui o banco de dados stackmobile que é o nome do seu banco













