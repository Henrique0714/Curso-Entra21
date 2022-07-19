import sqlite3
import requests

conexao =  sqlite3.connect('vendas.db')
cursor = conexao.cursor()


def CadastroC():
    novonome = input('Digite o nome do cliente novo:')
    cpf = input('Digite o CPF do cliente novo:')
    cep = input('Digite o cep do cliente novo:')
    CEP = requests.get(f'https://viacep.com.br/ws/{cep}/json/')


    cursor.execute('INSERT INTO clientes(nome_cliente, CPF_cliente, CEP_cliente, cidade, estado, rua)'
               'VALUES (?,?,?,?,?,?)', (novonome, cpf, cep, CEP.json()['localidade'], CEP.json()['uf'], CEP.json()['logradouro']))
    conexao.commit()
    cursor.execute('SELECT * FROM clientes')
    for clientes in cursor.fetchall():
        print(f'{clientes[0]} - {clientes[1]} - {clientes[2]} - {clientes[3]} - {clientes[4]} - {clientes[5]} - {clientes[6]}')


CadastroC()

def CadastroV():
    novonome = input('Digite a data da sua venda:')
    data = input('Digite a hora exata da venda::')
    cep = input('Digite o CPF do cliente:')
    cod = input('Digite o código de barras do produto:')
    quantidade = int(input('Digite a quantdade do produto:'))
    valor = int(input('Digite o valor do produto:'))
    total = quantidade * valor



    cursor.execute('INSERT INTO vendas(data_venda, hora, CPF_cliente, cod_barras, quantidade, valor_unitario, valor_total)'
                   'VALUES (?,?,?,?,?,?,?)',
                   (novonome, data, cep, cod, str(quantidade), str(valor), total))
    conexao.commit()
    cursor.execute('SELECT * FROM vendas')
    for vendas in cursor.fetchall():
        print(
            f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')

CadastroV()

#
#
# def CadastroP():
#     cod = input('Digite o código de barras:')
#     novoP = input('Digite o nome do produto a ser cadastrado:')
#     fabrica = input('Digite o fabricante:')
#
#     cursor.execute('INSERT INTO produtos(cod_barras, nome_produto, fabricante)'
#                    'VALUES (?,?,?)',
#                    (cod, novoP, fabrica))
#     conexao.commit()
#     cursor.execute('SELECT * FROM produtos')
#     for produtos in cursor.fetchall():
#         print(
#             f'{produtos[0]} - {produtos[1]} - {produtos[2]} - {produtos[3]}')
# # CadastroP()
#
