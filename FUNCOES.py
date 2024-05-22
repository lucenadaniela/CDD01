def funcao():
  print("Bloco de codigo")

def imprime_nome(nome):
    print(f'Nome: {nome}')

def piramide(numero):
    for x in range(1,numero+1):
        for y in range(1,x+1):
            print(x, end="")
        print()

def estoque (produto, quantidade, valor):
    valortotal = quantidade * valor
    return (valortotal)

def argumento(numero):
 if numero < 0:
    return ("N")
 elif numero > 0:
    return ("P")
 else:
    return ("Z")

def somar(x, y):
    soma = x+y
    return soma
def somar2(*numeros):
    soma = 0
    for i in range(len(numeros)):
        soma = soma + numeros[i]
    return soma

def contar_letras(frase):
    letras = 0
    for caractere in frase:
        if caractere not in " .,!":
            letras += 1
    return letras

def inverter_texto(frase):
    return frase[::-1]

