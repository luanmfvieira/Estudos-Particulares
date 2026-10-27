NoSQL (Not Only SQL) é um tipo de banco de dados que não usa exclusivamente o modelo relacional tradicional (tabelas) e é projetado para trabalhar com grandes volumes de dados não estruturados ou semiestruturados.

Características principais:
Não usa SQL como linguagem principal (ou usa parcialmente).

Não tem esquema fixo (schema-less).

Alta escalabilidade (ideal para sistemas distribuídos).

Suporta diferentes tipos de dados: documentos, chave-valor, grafos, colunas.

Tipos comuns de NoSQL:
Documentos (ex: MongoDB) → usa JSON ou BSON.

Chave-valor (ex: Redis) → simples par chave e valor.

Colunar (ex: Cassandra) → colunas ao invés de linhas.

Grafos (ex: Neo4j) → ideal para redes e conexões.

Quando usar NoSQL?
Dados não estruturados ou com estrutura variável.

Escalabilidade horizontal (muitos servidores).

Aplicações em tempo real, Big Data, redes sociais, etc.

----------------------------------------------------------------------------------

no mongo shell voce usou o comando

db.createCollection("collection")

para criar um database por lá

para limpar a tela do cmd é cls

------------------------------------------------------------------------

se o mongosh não for direto no cmd adicione ele ao path em variaveis do ambiente do sistema

-------------------------------------------------------------------------

comando

show collections   para ver as coleções dentro do seu database selecionado



para deletar uma collection

db.testeteste.drop()

db.dropDatabase()   para excluir o banco de dados que esta em use

--------------------------------------------------------------------------------



o mongodb coloca o id automaticamente



/** 
* Paste one or more documents here                                    o comando /**   e */ para abrir e fechar comentários
*/
{
  "_id": {
    "$oid": "68950b422facd248ab12d6cc"
  }
}



-------------------------------------------------------------------------------

{
  "_id": {
    "$oid": "68950e962facd248ab12d6cd"
  },
  "name": "Loroan",
  "email": "loroanlol@gmail.com",
  "password": "@Aguamineral50",
  "avatar": "Warrior",
  "game": "Sword Art Online",
  "highscore": 0,
  "money": 0.01,
  "hp": 0,
  "xp": 0,
  "level": 0
}

-------------------------------------------------------------------------------


no mongoshell  

db.users.insertOne({"marquinhos":10})


Caso você queira adicionar mais de uma lista de uma vez, usa-se

db.users.insertMany([{dados1},{dados2}])

-----------------------------------------------------

filtragem e busca

em project você pode filtar apenas por uma coluna fazendo assim

{name:1,email:1}
por padrão ele tras o id também

mostra apenas name e email

ou no primeiro campo para você pode digitar

{name:"Louroan"}

ele pegara toda a lista que contém isso

se usar
{name:0,email:0}

ele tras tudo menos essas duas colunas

em sort,

ordenar em ordem descrescente {name:-1 }  e crescente {name:1 }



em collation,

{locale:"pt",strength:2}

ignora caracteres especiais e letras maiusculas

atlas configura pelo site  uma ia para busca


----------------------------------------------------------

no shell

db.users.find({name:"Louroan"});

para pesquisa ele mostra a coluna inteira


db.users.find({name:"louroan"}).collation({locale:"pt",strength:2});

consulta com caracteres especiais


{$and:[{level:{$gte:0}},{game:"Sword Art Online"}]}

$gte

seleciona do nivel x e adiante


$and

para duas funções na mesmo busca


site manual do mongodb

https://www.mongodb.com/pt-br/docs/manual/reference/operator/query/

----------------------------------------------------------------------------



 db.users.find({name:"Louroan"});
[
  {
    _id: ObjectId('68950e962facd248ab12d6cd'),
    name: 'Louroan',
    email: 'loroanlol@gmail.com',
    password: '@Aguamineral50',
    avatar: 'Warrior',
    game: 'Sword Art Online',
    highscore: 0,
    money: 0.01,
    hp: 500,
    xp: 0,
    level: 0
  }
]


----------------------------------------------------------------------------


db.users.updateOne({name:"Louroan"},{$set:{highscore:600}});
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,                        <==== retorno do cmd
  upsertedCount: 0
}

----------------------------------------------------------------------------

db.users.updateMany({game:"Sword Art Online"},{$set:{highscore:100, hp:100, money:100, xp:1000}});



você deu update nas informações de todos os que estavam dentro do game citado



para consultar todos os documentos 

db.users.find({});



adicionei uma nova coluna em todos

 db.users.updateMany({},{$set:{item1:"Black Sword"}});



var id = ObjectId("68950e962facd248ab12d6cd");


criou a variavel para armazenar o id


db.users.updateOne({_id:id},{$set:{hp:200}});

deu update na variavel id que foi criada


----------------------------------------------------------------------------

Para deletar algo

db.users.deleteOne({name:"Louroan"});

ele retorna true


GameControll> var id = ObjectId("68950e962facd248ab12d6cd");

GameControll> db.users.deleteOne({_id:id});

acima, caso queira deletar tudo de uma id você transforma o id em uma variavel id e depois deleta ela


----------------------------------------------------------------------------

fiz uma configuração ao baixar o mongodbtools para quando abrir o cmd ja estar implementado

criando a pasta tools dentro de mongo db e colocando a bin

apos isso variaveis de ambiente e colocar o path de bin


----------------------------------------------------------------------------
Mongodump - para fazer backup de dados

abrir no cmd digitando mongodump

para fazer backup pelo dump digite no cmd

mongodump --db=GameControll --out=c:\curso

--db=nomedoquequerfazerbacukp --out=diretorio (cria a pasta com o nome caso ainda não haja)


o comando ficou  

mongodump --db=GameControll --out=C:\Users\Luan\Desktop\Main\dev


no comando abaixo eu especificio qual collection eu quero fazer backup em especifico

mongodump --db=GameControll --collection=users --out=C:\Users\Luan\Desktop\Main\dev


o comando exclude para fazer backup de tudo menos da mencionada

mongodump --db=GameControll --excludeCollection=users --out=C:\Users\Luan\Desktop\Main\dev


para restaurar todo o banco de dados

selecione o diretorio de onde esta ele no comando


mongorestore --db=GameControll C:\Users\Luan\Desktop\Main\dev\GameControll


-----------------------------------------------------------------------------------------------







