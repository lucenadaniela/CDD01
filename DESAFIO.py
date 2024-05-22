h1 = float(input("Digite hora 1: "))
min1 = float(input("Digite minuto 1: "))
h2 = float(input("Digite hora 2: "))
min2 = float(input("Digite minuto 2: "))
if h1 > h2:
    h1 = h1 - 12
if h2 > h1:
    h2 = h2 - 12
hora = h1 + h2
if hora > 12:
    hora = hora - 12
minutos = min1 + min2
if minutos >= 60:
    minutos = minutos - 60
    hora = hora + 1
print(hora, minutos)






