import sqlite3

conexao = sqlite3.connect('Meu primeiro banco.db')
cursor = conexao.cursor()
#CRIAR TABELA
# cursor.execute('CREATE TABLE IF NOT EXISTS frutas ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome_fruta TEXT,'
#                'variedade TEXT)')
#
# conexao.commit()
# #INSERIR DADOS NA TABELA
# cursor.execute('INSERT INTO frutas(nome_fruta, variedade)'
#                'VALUES ("Banana","Caturra")')
#
# conexao.commit()

#BUSCAR DADOS
#
# cursor.execute('UPDATE frutas SET variedade = "Branca" WHERE id = 3')
# conexao.commit()
#
# cursor.execute('SELECT * FROM frutas')
# for fruta in cursor.fetchall():
#     print(f'{fruta[0]} - {fruta[1]} - {fruta[2]}')
#
#DELETAR
# cursor.execute('DELETE FROM frutas')
# conexao.commit()

#DELETAR TABELA
# cursor.execute('DROP TABLE frutas')
# conexao.commit()



cursor.close()
conexao.close()