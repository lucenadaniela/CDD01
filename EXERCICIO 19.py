valor1 = float(input("Digite primeiro valor: "))
valor2 = float(input("Digite segundo valor: "))

while valor2 == 0:
    valor2 = float(input("Valor nao pode ser 0. Digite segundo valor: "))
divisao = valor1/valor2
print(f"Resultado {divisao}")