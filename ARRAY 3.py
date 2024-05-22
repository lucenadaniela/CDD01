"""ESCREVA UM CODIGO QUE PERMITA A LEITURA DAS NOTAS, DE UMA TURMA DE 5 ALUNOS E
GUARDE NUM VETOR. CALCULAR A MEDIA DA TURMA E CONTAR QUANTOS ALUNOS OBTIVERAM NOTA ACIMA
DESTA MEDIA CALCULADA. ESCREVER A MEDIA DA TURMA E O RESULTADO DA CONTAGE"""

notas = ["", "", "", "", ""]
somanotas = 0
cont = 0
for x in range(5):
    notas[x] = float(input("Digite sua nota: "))
for y in range(5):
    somanotas = somanotas + notas[y]
media = somanotas/5
for z in range(5):
 if notas[z] >= media:
  cont = cont +1
print(f"media da tuma é {media} e {cont} ficaram na media ou acima")







