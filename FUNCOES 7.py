"""FACA UMA FUNCAO QUE RECEBA UM TEXTO COMO ARGUMENTO, MOSTRE A QUANTIDADE DE LETRAS E TAMBEM IMPRIMA O TEXTO AO CONTRATRIO"""
def contar_letras(frase):
    letras = 0
    for caractere in frase:
        if caractere not in " .,!":
            letras += 1
    return letras

def inverter_texto(frase):
    return frase[::-1]

frase = input("Digite uma frase: ")
texto_invertido = inverter_texto(frase)
quantidade_letras = contar_letras(frase)
print(f'O texto invertido:{texto_invertido}. e a quantidades de letras é : {quantidade_letras}')