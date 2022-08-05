import sqlite3
import requests
# import cpf as cp
import cpf_tools as cp

conexao = sqlite3.connect('Vendas.db')
cursor = conexao.cursor()
lista_cpf = []
lista_codB = []


def CadastroC():
    cursor.execute('SELECT * FROM clientes')
    for clientes in cursor.fetchall():
        print(
            f'{clientes[0]} - {clientes[1]} - {clientes[2]} - {clientes[3]} - {clientes[4]} - {clientes[5]} - {clientes[6]}')
        lista_cpf.append(clientes[2])

    novonome = input('Digite o nome do cliente novo:')
    cpf = str(input('Digite o CPF do cliente novo:'))
    if cpf in lista_cpf:
        print('CPF já cadastrado, tente novamente!')
        CadastroC()
    else:
        cep = input('Digite o cep do cliente novo:')
        try:
            CEP = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            aa = cp.cpf_str_validation(cpf)
            if aa == False:
                print('CPF inválido, tente novamente.')
                CadastroC()
            else:
                cursor.execute('INSERT INTO clientes(nome_cliente, cpf_cliente, cep_cliente, cidade, estado, rua)'
                               'VALUES (?,?,?,?,?,?)', (novonome, cpf, cep, CEP.json()['localidade'], CEP.json()['uf'],
                                                        CEP.json()['logradouro']))
                conexao.commit()
                cursor.execute('SELECT * FROM clientes')
                for clientes in cursor.fetchall():
                    print(
                        f'{clientes[0]} - {clientes[1]} - {clientes[2]} - {clientes[3]} - {clientes[4]} - {clientes[5]} - {clientes[6]}')
                    lista_cpf.append(cpf)
                    # print(lista_cpf)
        except:
            print('CEP inválido, tente novamente!')
            CadastroC()


# CadastroC()

def CadastroV():
    cursor.execute('SELECT * FROM vendas')
    for vendas in cursor.fetchall():
        print(
            f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')
    cursor.execute('SELECT * FROM produtos[1]')
    for produtos in cursor.fetchall():
        lista_codB.append(produtos[1])
    novonome = input('Digite a data da sua venda:')
    data = input('Digite a hora exata da venda:')
    cpf = input('Digite o CPF do cliente:')
    cursor.execute('SELECT * FROM clientes[2]')
    for clientes in cursor.fetchall():
        lista_cpf.append(clientes[2])
    if cpf in lista_cpf:
        cod = input('Digite o código de barras do produto:')
        if len(cod) == 13:
            if cod in lista_codB:

                quantidade = int(input('Digite a quantdade do produto:'))
                valor = int(input('Digite o valor do produto:'))
                total = quantidade * valor

                cursor.execute(
                    'INSERT INTO vendas(data_venda, hora, cpf_cliente, cod_barras, quantidade, valor_unitario, valor_total)'
                    'VALUES (?,?,?,?,?,?,?)',
                    (novonome, data, cpf, cod, str(quantidade), str(valor), total))
                conexao.commit()
                cursor.execute('SELECT * FROM vendas')
                for vendas in cursor.fetchall():
                    print(
                        f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')
            else:
                print('Código de barras não registrado, tente novamente!')
                CadastroV()
        else:
            print('Código de barras inválido, tente novamente!')
            CadastroV()
    else:
        print('CPF do cliente não cadastrado!!!')
        CadastroV()


# CadastroV()


def CadastroP():
    cursor.execute('SELECT * FROM produtos')
    for produtos in cursor.fetchall():
        print(f'{produtos[0]} - {produtos[1]} - {produtos[2]} - {produtos[3]}')
    cod = input('Digite o código de barras:')
    cursor.execute('SELECT * FROM produtos[1]')
    for produtos in cursor.fetchall():
        lista_codB.append(produtos[1])
    if len(cod) == 13:
        if cod in lista_codB:
            print('Código de barras já registrado, tente novamente!')
            CadastroP()
        else:
            novoP = input('Digite o nome do produto a ser cadastrado:')
            fabrica = input('Digite o fabricante:')

            cursor.execute('INSERT INTO produtos(cod_barras, nome_produto, fabricante)'
                           'VALUES (?,?,?)',
                           (cod, novoP, fabrica))
            conexao.commit()
            cursor.execute('SELECT * FROM produtos')
            for produtos in cursor.fetchall():
                print(
                    f'{produtos[0]} - {produtos[1]} - {produtos[2]} - {produtos[3]}')
    else:
        print('Código de barras inválido, tente novamente!')
        CadastroP()


# CadastroP()


def AlterarC():
    cursor.execute('SELECT * FROM clientes')

    for clientes in cursor.fetchall():
        print(
            f'{clientes[0]} - {clientes[1]} - {clientes[2]} - {clientes[3]} - {clientes[4]} - {clientes[5]} - {clientes[6]}')

    quall = input('Digite o id do cliente que você quer editar:')
    qual = input('Digite o que você gostaria de mudar:\n'
                 '(1)Nome\n'
                 '(2)CPF do cliente\n'
                 '(3)CEP do cliente:')
    if qual == '1':
        novonome = input('Digite o novo nome do cliente:')
        cursor.execute(f'UPDATE clientes SET nome_cliente="{novonome}" WHERE id_cliente = "{quall}"')
        cursor.execute('SELECT * FROM clientes')
        conexao.commit()
        for clientes in cursor.fetchall():
            print(
                f'{clientes[0]} - {clientes[1]} - {clientes[2]} - {clientes[3]} - {clientes[4]} - {clientes[5]} - {clientes[6]}')

    if qual == '2':
        novocpf = input('Digite o novo CPF:')
        aa = cp.cpf_str_validation(novocpf)

        if aa == False:
            print('CPF inválido, tente novamente.')
            AlterarC()

        else:

            cursor.execute(f'UPDATE clientes SET cpf_cliente= "{novocpf}" WHERE id_cliente = {quall}')
            cursor.execute('SELECT * FROM clientes')
            conexao.commit()
            for clientes in cursor.fetchall():
                print(
                    f'{clientes[0]} - {clientes[1]} - {clientes[2]} - {clientes[3]} - {clientes[4]} - {clientes[5]} - {clientes[6]}')
    elif qual == '3':
        novocep = input('Digite o novo cep do cliente:')
        try:
            CEP = requests.get(f'https://viacep.com.br/ws/{novocep}/json/')
            cursor.execute(f'UPDATE clientes SET cep_cliente= "{novocep}" WHERE id_cliente= "{quall}"')
            novacity = CEP.json()['localidade']
            cursor.execute(f'UPDATE clientes SET cidade= "{novacity}" WHERE id_cliente= "{quall}"')
            novoestado = CEP.json()['uf']
            cursor.execute(f'UPDATE clientes SET estado= "{novoestado}" WHERE id_cliente= "{quall}"')
            novarua = CEP.json()['logradouro']
            cursor.execute(f'UPDATE clientes SET rua= "{novarua}" WHERE id_cliente= "{quall}"')
            conexao.commit()
            cursor.execute('SELECT * FROM clientes')
            for clientes in cursor.fetchall():
                print(
                    f'{clientes[0]} - {clientes[1]} - {clientes[2]} - {clientes[3]} - {clientes[4]} - {clientes[5]} - {clientes[6]}')
        except:
            print('Novo CEP inválido!')
            AlterarC()


# AlterarC()


def AlterarV():
    cursor.execute('SELECT * FROM vendas')
    for vendas in cursor.fetchall():
        print(
            f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')
    quall = input('Digite o id da venda que você quer mudar:')
    oq = input('Digite qual fator da venda você quer mudar:\n'
               '(1)Data;\n'
               '(2)Hora;\n'
               '(3)cpf_cliente;\n'
               '(4)Código de barras;\n'
               '(5)Quantidade;\n'
               '(6)Valor unitário;\n'
               '(7) Valor Total:')
    if oq == '1':
        novadata = input('Digite a data alterada:')
        cursor.execute(f'UPDATE vendas SET data_venda= "{novadata}" WHERE id_venda= "{quall}"')
        conexao.commit()
        cursor.execute('SELECT * FROM vendas')
        for vendas in cursor.fetchall():
            print(
                f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')

    if oq == '2':
        novahora = input('Digite a data alterada:')
        cursor.execute(f'UPDATE vendas SET hora= "{novahora}" WHERE id_venda= "{quall}"')
        conexao.commit()
        for vendas in cursor.fetchall():
            print(
                f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')

    if oq == '3':
        novocpf = input('Digite o CPF alterado:')
        aa = cp.cpf_str_validation(novocpf)

        if aa == False:
            print('CPF inválido, tente novamente.')
            AlterarV()

        else:

            cursor.execute(f'UPDATE vendas SET cpf_cliente= "{novocpf}" WHERE id_cliente = {quall}')
            conexao.commit()
            cursor.execute('SELECT * FROM vendas')
            for vendas in cursor.fetchall():
                print(
                    f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')

    if oq == '4':
        novocod = input('Digite o código de barras alterado:')
        if len(novocod) == 13:
            if novocod in lista_codB:
                cursor.execute(f'UPDATE vendas SET cod_barras= "{novocod}" WHERE id_venda= "{quall}"')
                conexao.commit()
                cursor.execute('SELECT * FROM vendas')
                for vendas in cursor.fetchall():
                    print(
                        f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')
            else:
                print('Código de barras não registrado!')
        else:
            print('Novo código de barras inválido!')
            AlterarV()

    if oq == '5':
        novaqtd = input('Digite a quantidade alterada:')
        cursor.execute(f'UPDATE vendas SET quantidade= "{novaqtd}" WHERE id_venda= "{quall}"')
        conexao.commit()
        cursor.execute('SELECT * FROM vendas')
        for vendas in cursor.fetchall():
            print(
                f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')

    if oq == '6':
        novovalor = input('Digite a data alterada:')
        cursor.execute(f'UPDATE vendas SET valor_unitario= "{novovalor}" WHERE id_venda= "{quall}"')
        conexao.commit()
        cursor.execute('SELECT * FROM vendas')
        for vendas in cursor.fetchall():
            print(
                f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')

    if oq == '7':
        novototal = input('Digite a data alterada:')
        cursor.execute(f'UPDATE vendas SET valor_total= "{novototal}" WHERE id_venda= "{quall}"')
        conexao.commit()
        cursor.execute('SELECT * FROM vendas')
        for vendas in cursor.fetchall():
            print(
                f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')


# AlterarV()


def AlterarP():
    cursor.execute('SELECT * FROM produtos')
    for produtos in cursor.fetchall():
        print(f'{produtos[0]} - {produtos[1]} - {produtos[2]} - {produtos[3]}')
    quall = input('Selecione o id do produto que você quer editar:')
    oq = input('Selecione a opção que você quer mudar:\n'
               '(1)Código de barras;\n'
               '(2)Nome do produto;\n'
               '(3)Fabricante')
    if oq == '1':
        novocod = input('Digite o código de barras alterado:')

        if len(novocod) == 13:
            cursor.execute(f'UPDATE produtos SET cod_barras="{novocod}" WHERE id_produto="{quall}"')
            conexao.commit()
            cursor.execute('SELECT * FROM produtos')
            for produtos in cursor.fetchall():
                print(f'{produtos[0]} - {produtos[1]} - {produtos[2]} - {produtos[3]}')
        else:
            print('Novo código inválido')

    if oq == '2':
        novonome = input('Digite o nome do produto alterado:')
        cursor.execute(f'UPDATE produtos SET nome_produto="{novonome}" WHERE id_produto="{quall}"')
        conexao.commit()
        cursor.execute('SELECT * FROM produtos')
        for produtos in cursor.fetchall():
            print(f'{produtos[0]} - {produtos[1]} - {produtos[2]} - {produtos[3]}')

    if oq == '3':
        novonome = input('Digite o fabricante do produto alterado:')
        cursor.execute(f'UPDATE produtos SET fabricante="{novonome}" WHERE id_produto="{quall}"')
        conexao.commit()
        cursor.execute('SELECT * FROM produtos')
        for produtos in cursor.fetchall():
            print(f'{produtos[0]} - {produtos[1]} - {produtos[2]} - {produtos[3]}')


# AlterarP()

def DeletarC():
    cursor.execute('SELECT * FROM clientes')
    for clientes in cursor.fetchall():
        print(
            f'{clientes[0]} - {clientes[1]} - {clientes[2]} - {clientes[3]} - {clientes[4]} - {clientes[5]} - {clientes[6]}')

    quall = input('Selecione o id do cliente que você quer excluir:')
    cursor.execute(f'DELETE FROM clientes WHERE id_cliente={quall}')
    conexao.commit()
    cursor.execute('SELECT * FROM clientes')
    for clientes in cursor.fetchall():
        print(
            f'{clientes[0]} - {clientes[1]} - {clientes[2]} - {clientes[3]} - {clientes[4]} - {clientes[5]} - {clientes[6]}')


# DeletarC()

def DeletarV():
    cursor.execute('SELECT * FROM vendas')
    for vendas in cursor.fetchall():
        print(
            f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')
    quall = input('Selecione o id da venda que você quer excluir:')
    cursor.execute(f'DELETE FROM vendas WHERE id_venda={quall}')
    conexao.commit()
    cursor.execute('SELECT * FROM vendas')
    for vendas in cursor.fetchall():
        print(
            f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')


# DeletarV()

def DeletarP():
    cursor.execute('SELECT * FROM produtos')
    for produtos in cursor.fetchall():
        print(f'{produtos[0]} - {produtos[1]} - {produtos[2]} - {produtos[3]}')
    quall = input('Selecione o id do produto que você quer excluir:')
    cursor.execute(f'DELETE FROM produtos WHERE id_produto={quall}')
    conexao.commit()
    cursor.execute('SELECT * FROM produtos')
    for produtos in cursor.fetchall():
        print(f'{produtos[0]} - {produtos[1]} - {produtos[2]} - {produtos[3]}')


# DeletarP()


lista_vendasCPF = []
lista_clientes = []


def ListarV(cpff):
    cpff = input('Qual CPF você quer verificar:')
    cursor.execute(f'SELECT * FROM vendas  WHERE cpf_cliente = "{cpff}"')
    for vendas in cursor.fetchall():
        print(
            f'{vendas[0]} - {vendas[1]} - {vendas[2]} - {vendas[3]} - {vendas[4]} - {vendas[5]} - {vendas[6]} - {vendas[7]}')


# ListarV(cpf)

while True:

    oq_quer = input('Digite o que você deseja:\n'
                    '(1) Cadastrar cliente;\n'
                    '(2) Cadastrar venda;\n'
                    '(3) Cadastrar produto;\n'
                    '(4) Alterar informação do cliente;\n'
                    '(5) Alterar informação de uma venda;\n'
                    '(6) Alterar informação de um produto;\n'
                    '(7) Deletar cliente;\n'
                    '(8) Deletar venda;\n'
                    '(9) Deletar produto;\n'
                    '(10) Listar venda por CPF;\n'


                    '(11) Finalizar;\n'
                    '')
    if oq_quer == '1':
        CadastroC()
        cont = input('Deseja continuar?\n (1)Sim\n (2)Não\n')
        if cont == '1':
            continue
        if cont == '2':
            print('Trabalho concluído')
            break
    if oq_quer == '2':
        CadastroV()
        cont = input('Deseja continuar?\n (1)Sim\n (2)Não\n')
        if cont == '1':
            continue
        if cont == '2':
            print('Trabalho concluído')
            break
        continue
    if oq_quer == '3':
        CadastroP()
        cont = input('Deseja continuar?\n (1)Sim\n (2)Não\n')
        if cont == '1':
            continue
        if cont == '2':
            print('Trabalho concluído')
            break
    if oq_quer == '4':
        AlterarC()
        cont = input('Deseja continuar?\n (1)Sim\n (2)Não\n')
        if cont == '1':
            continue
        if cont == '2':
            print('Trabalho concluído')
            break
    if oq_quer == '5':
        AlterarV()
        cont = input('Deseja continuar?\n (1)Sim\n (2)Não\n')
        if cont == '1':
            continue
        if cont == '2':
            print('Trabalho concluído')
            break
    if oq_quer == '6':
        AlterarP()
        cont = input('Deseja continuar?\n (1)Sim\n (2)Não\n')
        if cont == '1':
            continue
        if cont == '2':
            print('Trabalho concluído')
            break
    if oq_quer == '7':
        DeletarC()
        cont = input('Deseja continuar?\n (1)Sim\n (2)Não\n')
        if cont == '1':
            continue
        if cont == '2':
            print('Trabalho concluído')
            break
    if oq_quer == '8':
        DeletarV()
        cont = input('Deseja continuar?\n (1)Sim\n (2)Não\n')
        if cont == '1':
            continue
        if cont == '2':
            print('Trabalho concluído')
            break
    if oq_quer == '9':
        DeletarP()
        cont = input('Deseja continuar?\n (1)Sim\n (2)Não\n')
        if cont == '1':
            continue
        if cont == '2':
            print('Trabalho concluído')
            break
    if oq_quer == '10':
        ListarV()
        cont = input('Deseja continuar?\n (1)Sim\n (2)Não\n')
        if cont == '1':
            continue
        if cont == '2':
            print('Trabalho concluído')
            break


    if oq_quer == '11':
        print('Trabalho concluído')
        break
    else:
        print('Resposta inválida')
        break



