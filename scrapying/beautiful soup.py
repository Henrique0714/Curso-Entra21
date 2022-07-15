# from bs4 import BeautifulSoup
# import requests
# from operator import itemgetter
#
# produtos = []
# valores = []
# geral = []
#
# for i in range(100):
#     alvo = f'https://www.bistek.com.br/bebidas/vinhos-e-espumantes.html?p=2'
#     resposta = requests.get(alvo)
#     html = BeautifulSoup(resposta.text, 'html.parser')
#
#     for produto in html.select('.product-item-link'):
#         produtos.append(produto.text.replace("  ", '').replace('\n', ''))
#
#     for valor in html.select('.price-wrapper .price'):
#         valores.append(float(valor.text.replace('.', '').replace(',', '.').replace('R$ ', '')))
#
# for i in range(len(produtos)):
#     print(f'{produtos[i]} + {valores[i]}')
#
# for i in range(len(produtos)):
#     novo_registro = {"Produto" : produtos[i], 'Valor': valores[i]}
#     geral.append(novo_registro)
#
# lista_final = sorted(geral, key=itemgetter('Valor'), reverse = True)
#
# for i in lista_final:
#     print(i)

from bs4 import BeautifulSoup
import requests
from operator import itemgetter

itens = f'https://www.havan.com.br/celulares-e-smartphones/?departamentosHV='
resposta = requests.get(itens)
html = BeautifulSoup(resposta.text, 'html.parser')
print(resposta)

produtos = []
valores = []
geral = []

for produto in html.select('.product-item-link'):
    produtos.append(produto.text.replace('  ', '').replace('\n', ''))

for valor in html.select('.special-price .price'):
    valores.append(float(valor.text.replace('  ', '').replace('R$\xa0','').replace('.','').replace(',','.')))

for i in range(len(produtos)):
    # print(f'{produtos[i]} + {valores[i]}')
    novo_registro = {'Produto': produtos[i], 'Valor': valores[i]}
    geral.append(novo_registro)
lista_final = sorted(geral, key=itemgetter('Valor'))


for i in lista_final:
    print(i)