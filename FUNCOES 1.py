#criando a funcao
def piramide(numero):
    for x in range(1,numero+1):
        for y in range(1,x+1):
            print(x, end="")
        print()
#usando a funcao
opcao = int(input("Digite um numero: "))
piramide(opcao)



