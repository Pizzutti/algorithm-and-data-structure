from Cidade import Cidade
class Pessoa:

    def __init__(self, nome, idade=18, cid = Cidade(None, "Tangamandapio")):
        self.nome = nome
        self.idade = idade
        self.cidade = cid
        print( "Pessoa " , self.nome, " construída")