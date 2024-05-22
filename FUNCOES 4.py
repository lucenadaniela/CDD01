"""CRIE UMA FUNCAO QUE RECEBE O NOME DE UM PRODUTO, A QUANTIDADE QUE TEM NO ESTOQUE E O VALOR UNITARIO DO PRODUTO.
RETORNE O VALOR TOTAL DO MEU ESTOQUE."""

def estoque (produto, quantidade, valor):
    valortotal = quantidade * valor
    return (valortotal)

produto = input("Produto: ")
quantidade = int(input("Quantidade: "))
valor = float(input("Valor: "))
valorproduto1 = estoque(produto, quantidade, valor)
print(f"Valor total do produto é {valorproduto1}")


