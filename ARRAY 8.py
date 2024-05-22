"""Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array
diferente, após completar a digitação, imprimir , nome, senha e posição dos dados no array"""

nome = ["", "", "", "", ""]
senhas = ["", "", "", "", ""]
print("Cadastro")
for a in range (5):
    nome[a] = input("Digite seu usuario: ")
    senhas[a] = int(input("Digite sua senha: "))
for b in range(5):
    print(nome[b], senhas[b])