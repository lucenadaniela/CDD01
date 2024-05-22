import requests

print("Verificando endereço")
cep = input("Digite CEP: ")
if len(cep) != 8:
    print("CEP invalido")
    exit()
consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json')
print(consulta.json())
