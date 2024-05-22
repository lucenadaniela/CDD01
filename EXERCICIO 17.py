somanotas = 0
qnt = 0
contador = 0
while contador < 10:
    n = float(input("Digite a nota: "))
    if n >=0 and n <=10:
     somanotas = somanotas + n
     qnt = qnt + 1
    contador = contador + 1
media = somanotas/qnt

print(f"media igual a : {media}")