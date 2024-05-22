"""FAÇA UM CODIGO PARA LER 5 NOMES DE USUARIOS E SUAS RESPECTIVAS SENHAS, E ARMAZENAR CADA LISTA EM UM ARRAY DIFERENTE,
APOS COMPLETAR A DIGITAÇÃO, IMPRIMIR, NOME, SENHA E A POSIÇÃO DOS DADOS DO ARRAY"""

nome = ["", "", "", "", ""]
senhas = ["", "", "", "", ""]
for a in range (5):
    nome[a] = input("Digite seu usuario: ")
    senhas[a] = int(input("Digite sua senha: "))
for b in range (5):
    print(nome[b], senhas[b], b)