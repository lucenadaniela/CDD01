"""FACA UM PROGRAMA, COM UMA FUNCAO QUE NECESSITE DE UM ARGUMENTO.
A FUNCAO RETORNA O VALOR DE CARACTERE P, SE SEU ARGUMENTO FOR POSITIVO, E N, SE SEU ARGUMENTO FOR NEGATIVO
E Z SE O ARGUMENTO FOR ZERO"""

def argumento(numero):
 if numero < 0:
    return ("N")
 elif numero > 0:
    return ("P")
 else:
    return ("Z")

numero = int(input("Digite um numero: "))
mostrar = argumento(numero)
print(mostrar)