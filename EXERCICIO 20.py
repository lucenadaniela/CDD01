senha = 120199
tentativas = 0
tentativa1 = float(input("Digite senha: "))
if tentativa1 == senha:
 print("Acesso liberado")
else:
  while tentativas < 2:
    tentativa1 = float(input("ERRO. Digite sua senha novamente: "))
  if tentativa1 == senha:
    print("Acesso liberado")
    tentativas+=1
print("ACESSO BLOQUEADO")





