"""FAÇA UMA FUNCAO QUE RECEBA 2 ARGUMENTOS E ADICIONE CADA UM NUMA LISTA DIFERENTE. PRODUTO E PREÇO.
O SISTEMA DEVE PEDIR OS DADOS E APÓS ISSO VERIFICAR SE O USUARIO AINDA PRETENDE INSERIR MAIS PRODUTOS.
QUANDO TERMINAR DE INSERIR, IMPRIMIR AS LISTAS"""

produtos=[]
precos=[]

def estoque(nome, preco):
    produtos.append(nome)
    precos.append(preco)

