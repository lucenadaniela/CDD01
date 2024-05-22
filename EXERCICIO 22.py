resposta = "sim"
while resposta == "sim":
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
       nota1 = float(input("Nota invalida. Digite novamente primeira nota: "))

    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Nota invalida. Digite novamente segunda nota: "))

    media = (nota1+nota2)/2
    print(media)
    resposta = input("Deseja fazer o calculo novamente? ")
