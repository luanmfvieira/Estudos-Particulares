'''
Criar a classe carro com 3 propriedades para a classe e 3 metodos para ela
'''

class Carro:
    def __init__(self, cor, nome, embreagem):
        self.cor = cor
        self.nome = nome
        self.embreagem = embreagem

    def Acelerar(self):
        print('Aumentando os kms')

    def Reduzir(self):
        print('Reduzindo os kms')
    
    def Exibirinformacoesdocarro(self):
        print(self.cor, self.nome, self.embreagem)

carro1 = Carro('Preto', 'Honda civic', 'Automático')
carro1.Acelerar()
carro1.Reduzir()
carro1.Exibirinformacoesdocarro()


        




