
def piramide_sequencia(num):
 for linha in range(1,num+1,1):
    for coluna in range(1,linha+1):
        print(coluna, end="")
    print()

num = int(input("Digite um numero "))
piramide_sequencia(num)