contador = 0
somanotas = 0
qnt = 0

alunos = int(input("Digite o numero de alunos: "))

while contador < alunos:
   notas = int(input("qual sua nota?"))
   if notas >= 0 and notas <= 10:
    somanotas = somanotas + notas
    qnt = qnt + 1
   contador = contador + 1
media = somanotas/qnt

print(media)

