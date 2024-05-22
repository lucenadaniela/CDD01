contador = 0

for n in range(1,11,1):
    num = int(input("Digite numeros: "))
    if num < 0:
        contador = contador + 1
        print(contador)