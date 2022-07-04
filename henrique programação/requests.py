import output as output
import requests as requests

ender = input('Insira o seu CEP:\n')
CEP = requests.get(f'https://viacep.com.br/ws/{ender}/json/')
print()
print('Endereço:', CEP.json()['logradouro'])
print('Estado:', CEP.json()['uf'])
print('Bairro:', CEP.json()['bairro'])
print('Cidade:', CEP.json()['localidade'])
print('DDD:', CEP.json()['ddd'])
