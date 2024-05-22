"""FAÇA UM CODIGO PARA LER 5 NUMEROS E ARMAZENAR EM UM VETOR. APOS A LEITURA TOTAL DOS 5 NUMEROS,
O CODIGO DEVE ESCREVER ESSES 5 NUMEROS LIDOS NA ORDEM INVERSA"""

vetora = ["", "", "", "", ""]
for a in range(5):
    vetora[a] = float(input("Digite um numero: "))
for b in range(4,-1,-1):
    print(vetora[b])


