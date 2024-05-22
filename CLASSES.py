class Pessoa():
    def __init__(self, nomeAluno, idadeAluno, pesoAluno, comendo=False, falando=True, andando=True):
        self.nome=nomeAluno
        self.peso=pesoAluno
        self.idade=idadeAluno
        self.comendo=False
        self.falando=False
        self.andando=False
    def comer(self, alimento):
        if self.comendo == False:
         print(f'{self.nome} está comendo {alimento}')
         self.comendo=True
        else:
         print(f'{self.nome} já está comendo')
    def pararComer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer")
            self.comendo=False
    def falar(self, frase):
        if self.comendo == False:
         print(f'{self.nome} está falando: {frase}')
        else:
         print(f'{self.nome} está comendo, não pode falar.')


"""crie uma classe chamada Forma, que possui os atributos area e perimetro.
- implemente as subclasses Retangulo e Triangulo, que devem conter os metodos CalculaArea e CalculaPerimetro.
A classe triangulo deve ser deve ter tambem o atributo altura.
- No codigo de teste crie um objeto da classe triangulo e outro da classe retangulo. Calcule a area de cada um."""

class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0
class Retangulo(Forma):
    def __init__ (self):
        super().__init__()
    def areaCalcular(self, base, altura):
        self.area=base*altura
        print(f"A area do retangulo é {self.area}")
    def perimetroCalcular(self, base, altura):
        self.perimetro=2*(base+altura)
        print(f' O perimetro do retangulo é {self.perimetro}')
class Triangulo(Forma):
    def __init__ (self):
        self.altura = 0
        super(). __init__()
    def areaCalcular(self, base, altura):
        self.altura=altura
        self.area=(base*self.altura)/2
        print(f"A area do triangulo é {self.area}")
    def perimetroCalcular(self, lado):
        self.perimetro=lado*3
        print(f' O perimetro do triangulo é {self.perimetro}')


class Atleta:
    def __init__ (self, peso):
        self.aposentado = False
        self.peso = peso
        self.aquecimento = False
    def aquecer (self):
         self.aquecer = True
         print(f'Atleta AQUECER')
    def aposentar (self):
         self.aposentar = True
         print(f'Atleta APOSENTAR')

class Corredor (Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.correndo = False
    def correr (self):
        if self.aposentado == False:
            if self.aquecimento == True:
                self.corredor=True
                print(f'Atleta CORRENDO')
            else:
                print (f'Não pode correr, Atleta nao aqueceu')
    def pararCorrer (self):
        if self.corredor == True:
            self.corredor == False
            print(f'Atleta PARAR DE CORRER')
        else:
            print(f'Atleta JA ESTA PARADO')













