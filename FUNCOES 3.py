"""FACA UMA FUNCAO QUE CONTE QUANTAS VOGAIS TEM NUM TEXTO"""
texto = "o rato roeu a roupa do rei de roma"

def vogais(texto):
 cont=0
 y = "aeiouAEIOU"
 for x in texto:
    if x in y:
     cont = cont+1
 print(cont)

texto = "o rato roeu a roupa do rei de roma"
vogais(texto)