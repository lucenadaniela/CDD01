dentro=0
fora=0
for n in range(1,11,1):
    num = int(input("Digite numeros: "))
    if num >=10 and num <=20:
        dentro=dentro+1
fora = 10-dentro

print("dentro: ", dentro, "\n", "fora: ", fora)