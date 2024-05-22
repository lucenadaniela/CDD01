from CLASSES import *

p1 = Pessoa("Joao", 75, 35)
p2 = Pessoa ("Maria", 55, 23)
print(f'nome: {p1.nome}, idade: {p1.idade}, peso: {p1.peso}')
print(f'nome: {p2.nome}, idade: {p2.idade}, peso: {p2.peso}')

#alterar atributos:
p2.peso=60
#print novamente
print(f'nome: {p2.nome}, idade: {p2.idade}, peso: {p2.peso}')


p1.comer("Uva")
p1.pararComer()
p1.falar("Oi")

areatriangulo = Triangulo()
areatriangulo.areaCalcular(5,5)

perimetrotriangulo = Triangulo()
perimetrotriangulo.perimetroCalcular(5)

atleta1 = Atleta()





