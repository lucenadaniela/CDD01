"""PREENCHER UM VETOR A COM 10 NUMEROS. LOGO EM SEGUIDA, LER MAIS UM NUMERO E GUARDAR EM UMA VARIAVEL X
ARMAZENAR EM UM VETOR M O RESULTADO DE CADA ELEMENTO DE A MULTIPLICADO PELO VALOR X. NO FINAL IMPRIMIR O VETOR M."""

vetora = ["","","","","","","","","",""]
vetorm = ["","","","","","","","","",""]
for a in range (10):
   vetora[a] = float(input("Digite um numero: "))
x = float(input("Digite o multiplicador: "))
for b in range(10):
    vetorm[b] = vetora[b]*x
print(vetorm)





