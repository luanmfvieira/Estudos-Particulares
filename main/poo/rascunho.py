#todas as funçoes da class precisam de um self para ter acesso aos atributos
#em outras linguagens o __init__ é construtor
#o self sempre é ignorado como parametro e é usado apenas dentro da class

'''class Cliente:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir(self):
        print(self.nome, self.email)

luan = Cliente('Luan', 'luanmiguel.contato@outlook.com')

luan.exibir()
'''

'''from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

    def exibir(self):
        print(f'meu nome é {self.nome}, meu e-mail é {self.email} e minha idade é {self.idade}')

lu = Cliente(nome='Luan', email='luanmiguel.contato@outlook.com', idade='25')


lu.exibir()'''



