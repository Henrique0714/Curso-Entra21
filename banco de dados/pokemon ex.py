import sqlite3

conexao = sqlite3.connect('banco pokemon.db')
cursor = conexao.cursor()

conexao.commit()
listaP = []
# nome = input('Digite o nome do seu pokemon:')
# tipo = input('Digite o tipo do seu pokemon:')
# pokedex = input('Digite a pokedex do seu pokemon:')
# level = input('Digite o level do seu pokemon:')

def Inserir_Pokemon():
    cursor.execute('INSERT INTO lista_pokemons (nome, tipo, pokedex, level)'
                'VALUES(?,?,?,?)', (input('Digite o nome do seu pokemon:'),
                                    input('Digite o tipo do seu pokemon:'),
                                    input('Digite a pokedex do seu pokemon:'),
                                    int(input('Digite o level do seu pokemon:'))))

    conexao.commit()

    cursor.execute('SELECT * FROM lista_pokemons')
    for lista_pokemons in cursor.fetchall()A:
        print(f'{lista_pokemons[0]} - {lista_pokemons[1]} - {lista_pokemons[2]} - {lista_pokemons[3]} - {lista_pokemons[4]}')




# Inserir_Pokemon()


def Evolucao():
    qual = input('Digite o id do pokemon que você quer evoluir:')
    levelM = input('Digite para qual level vocêr quer evoluir o seu pokemon:')
    cursor.execute(f'UPDATE lista_pokemons SET Level= {levelM} WHERE id={qual}')
    conexao.commit()

    cursor.execute('SELECT * FROM lista_pokemons')
    for lista_pokemons in cursor.fetchall():
        print(f'{lista_pokemons[0]} - {lista_pokemons[1]} - {lista_pokemons[2]} - #{lista_pokemons[3]} - {lista_pokemons[4]}')

    conexao.commit()

# Evolucao()


def Listar():
    cursor.execute('SELECT * FROM lista_pokemons[1]')
    for lista_pokemons in cursor.fetchall():
        listaP.append(lista_pokemons[1])
    print(f'Os seus pokemons são {listaP}')


# Listar()


def Del():
    id = input('Digite o id do pokemon que você quer deletar:')
    cursor.execute(f'DELETE FROM lista_pokemons WHERE id={id}')
    conexao.commit()

    cursor.execute('SELECT * FROM lista_pokemons')
    for lista_pokemons in cursor.fetchall():
        print(f'{lista_pokemons[0]} - {lista_pokemons[1]} - {lista_pokemons[2]} - #{lista_pokemons[3]} - {lista_pokemons[4]}')


# Del()


def Edit():
    cursor.execute('SELECT * FROM lista_pokemons')
    for lista_pokemons in cursor.fetchall():
        print(f'{lista_pokemons[0]} - {lista_pokemons[1]} - {lista_pokemons[2]} - #{lista_pokemons[3]} - {lista_pokemons[4]}')
    qual = input('Digite o id do pokemon que você quer editar:')
    linha = input('Digite a opcão que você que editar:\n'
                  '(1) Nome;\n'
                  '(2) Tipo;\n'
                  '(3) Pokedex;\n'
                  '-')
    if linha == '1':
        novonome = input('Digite o novo nome para esse pokemon:')
        cursor.execute(f'UPDATE lista_pokemons SET nome= "{novonome}" WHERE id="{qual}"')

        cursor.execute('SELECT * FROM lista_pokemons')
        for lista_pokemons in cursor.fetchall():
            print(
                f'{lista_pokemons[0]} - {lista_pokemons[1]} - {lista_pokemons[2]} - #{lista_pokemons[3]} - {lista_pokemons[4]}')


    elif linha == '2':
        novotipo = input('Digite o novo nome para esse pokemon:')
        cursor.execute(f'UPDATE lista_pokemons SET tipo= "{novotipo}" WHERE id="{qual}"')

        cursor.execute('SELECT * FROM lista_pokemons')
        for lista_pokemons in cursor.fetchall():
            print(f'{lista_pokemons[0]} - {lista_pokemons[1]} - {lista_pokemons[2]} - #{lista_pokemons[3]} - {lista_pokemons[4]}')

    elif linha == '3':
        novapoke = input('Digite o novo nome para esse pokemon:')
        cursor.execute(f'UPDATE lista_pokemons SET tipo= "{novapoke}" WHERE id="{qual}"')

        cursor.execute('SELECT * FROM lista_pokemons')
        for lista_pokemons in cursor.fetchall():
            print(
                f'{lista_pokemons[0]} - {lista_pokemons[1]} - {lista_pokemons[2]} - #{lista_pokemons[3]} - {lista_pokemons[4]}')

Edit()