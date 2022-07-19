import sqlite3
conexao = sqlite3.connect('Banco de dados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'CPF TEXT,'
               'nome TEXT,'
               'data_nascimento TEXT,'
               'CEP TEXT,'
               'peso REAL,'
               'altura REAL)')
conexao.commit()

cpf = input('digite o CPF: ')
nome = input('digite o nome: ')
data_nascimento = input('digite a data de nascimento: ')
cep = input('digite o CEP: ')
peso = input('digite o peso: ')
altura = input('digite a altura: ')

cursor.execute('INSERT INTO clientes (cpf, nome, data_nascimento, cep, peso, altura)'
               'VALUES(?,?,?,?,?,?)',(cpf, nome, data_nascimento, cep, peso, altura))
conexao.commit()

cursor.execute('SELECT * FROM clientes')
for cliente in cursor.fetchall():
    print(f'{cliente[0]} - {cliente[2]} - {cliente[3]} - {cliente[4]} - {cliente[5]} - {cliente[6]}')

cursor.close()
conexao.close()
