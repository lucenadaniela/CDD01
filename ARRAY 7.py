"""ALTERE O SISTEMA ANTERIOR E FAÇA UM SITEMA DE LOGIN, PEDINDO A SENHA DO USUARIO E MOSTRANDO SEU NOME E A MENSSAGEM,
LOGIN EFETUADO COM SUCESSO"""
nome = ["", "", "", "", ""]
senhas = ["", "", "", "", ""]
for a in range (5):
    print("Cadastro")
    nome[a] = input("Digite seu usuario: ")
    senhas[a] = int(input("Digite sua senha: "))
for b in range (5):
    print(nome[b], senhas[b], b)