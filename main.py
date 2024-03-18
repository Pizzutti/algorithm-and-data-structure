# from Pessoa import Pessoa

# p1 = Pessoa( "Maria" , 25 )
# print( "Nome da Pessoa: ", p1.nome)
# p2 = Pessoa( idade="20" , nome="João" )
# p3 = Pessoa( "Carlos" )
# print("Idade do ",p3.nome," é: ", p3.idade)

from Cidade import Cidade
from Pessoa import Pessoa

c1 = Cidade()
c2 = Cidade( nome = "Porto Alegre")
c3 = Cidade(1, "Capao da Canoa")

print(c1)
c1.nome = "POA"
print(c1)
print(c2)
print(c3)

p1 = Pessoa("Lucas")
p2 = Pessoa("Lucas", 29)
p3 = Pessoa("Lucas", 30, c1)
p4 = Pessoa("Hortencia", cid= c2)
p5 = Pessoa("hortencia", idade = 23)