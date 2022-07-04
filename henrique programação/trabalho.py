# import remi
# import PySimpleGUI as sg
# from time import sleep

# output.clear()
# for i in CEP.json():
#   print(CEP.json()[i])

# Layout
sg.theme('Reddit')
cont = 0
layout = [
    [sg.Frame('', [[sg.Text('CENTRAL DOS INSCRITOS', justification='c', font='20', pad=20)],
                   [sg.Text('Nome:', s=(35, 1), justification='l')],
                   [sg.Input(key='usuario', s=(40, 1))],
                   [sg.Text('Senha:', s=(35, 1), justification='l')],
                   [sg.Input(key='senha', s=(40, 1), password_char='*')],
                   [sg.Button('Login', key='salvar', expand_x=True)],
                   [sg.Button('Cadastrar', key='cadastro', expand_x=True)],
                   [sg.Text("", key="mensagem")]], pad=30, border_width=4)]
]

layout_principal_l = [
    [sg.Text('CPF', size=(19, 1), justification='c')],
    [sg.Input(key='cpf', s=(21, 1))],
    [sg.Text('GENERO', size=(19, 1), justification='c')],
    [sg.Combo(['Homem', 'Mulher', 'Não Binário', 'Mulher Trans', 'Homem Trans'], s=(19, 1), readonly=True)],
    [sg.Text('EMAIL', size=(19, 1), justification='c')],
    [sg.Input(key='email', s=(21, 1))],
    [sg.Text('COR', size=(19, 1), justification='c')],
    [sg.Combo(['Preto', 'Branco', 'Pardo', 'Amarelo'], s=(19, 1), key='raca', readonly=True)],
    [sg.Text('ALGUMA DEFICIENCIA?', size=(19, 1), justification='c')],
    [sg.Radio('sim', 'opc'), sg.Radio('nao', 'opc', s=(8, 1))],
    [sg.Text('NOME DO PAI', size=(19, 1), justification='c')],
    [sg.Input(key='nome do pai', s=(21, 1))],
    [sg.Text('NOME DA MÃE', size=(19, 1), justification='c')],
    [sg.Input(key='nome mãe', s=(21, 1))]
]
layout_principal_r = [
    [sg.Text('DATA DE NASCIMENTO', size=(20, 1))],
    [sg.Input(key='dat nasc', s=(22, 1))],
    [sg.Text('WPP')],
    [sg.Input(key='wpp', s=(21, 1))],
    [sg.Text('CONFIRM EMAIL')],
    [sg.Input(key='c-email', s=(21, 1))],
    [sg.Text('ESTADO CIVIL')],
    [sg.Combo(['CASADO(A)', 'SOLTEIRO(A)', 'SEPARADO(A)', 'VIUVO(A)'], s=(19, 1), key='estado')],
    [sg.Text('QUAL?')],
    [sg.Input(key='qual', size=(21, 1))],
    [sg.Text('PROFISSÃO DO PAI', size=(20, 1))],
    [sg.Input(key='profissão do pai', s=(21, 1))],
    [sg.Text('PROFISSÃO DA MÃE', size=(20, 1))],
    [sg.Input(key='profissão mãe', s=(21, 1))],

    # [sg.Text('CEP', size=(15, 1)), sg.Text('RUA', size=(15, 1)), sg.Text('NUMERO', size=(10, 1))],
    # [sg.Input(key='cep', s=(15, 1)), sg.Input(key='rua', s=(15, 1)), sg.Input(key='numero', s=(10, 1))],
    #
    # [sg.Text('BAIRRO', size=(21, 1)), sg.Text('COMPLEMENTO', size=(20, 1))],
    # [sg.Input(key='bairro', s=(21, 1)), sg.Input(key='complemento', s=(21, 1))],
    # [sg.Text('ESTADO', size=(21, 1)), sg.Text('CIDADE', size=(20, 1))],
    # [sg.Input(key='estado', s=(21, 1)), sg.Input(key='cidade', s=(21, 1))],
    # [sg.Text('ESTADO NATURALIDADE', size=(21, 1)), sg.Text('CIDADE NATURALIDADE', size=(20, 1))],
    # [sg.Combo(['Preto', 'Branco', 'Pardo', 'Amarelo'], s=(19, 1)), sg.Combo(['CASADO(A)', 'SOLTEIRO(A)', 'SEPARADO(A)', 'VIUVO(A)'], s=(19, 1))],
]

layout_principal = [
    [sg.TabGroup([[sg.Tab('Cadastro', [[sg.Text('INSIRA SEUS DADOS')],
                                       [sg.Text('NOME COMPLETO', font=18, s=(40, 1), justification='c')],
                                       [sg.Input(key='nome completo', s=(30, 1), font=22, justification='c',
                                                 expand_x=True), ],
                                       [sg.Col(layout_principal_l), sg.Col(layout_principal_r)],
                                       [sg.Button('Salvar'), sg.Button('Parar')]])]])]
]
layout_cadastro = [
    [sg.Frame('', [[sg.Text('Nome'), sg.Input(key='usuario_cadastro')],
                   [sg.Text('Senha'), sg.Input(key='senha_cadastro', password_char='*')],
                   [sg.Button('Cadastrar', key='salvar_cadastro')],
                   [sg.Text("", key="mensagem")]], pad=30)]
]

janela = sg.Window('Tela de Cadastro', layout, element_justification='c', background_color='Blue')
# janela
while True:
    eventos, valores = janela.read()

    if eventos == 'cadastro':  # Clicou no botao CADASTRO

        janela_cadastro = sg.Window('Tela de Cadastro', layout_cadastro, element_justification='c',
                                    background_color='Blue')
        while True:
            eventos_cadastro, valores_cadastro = janela_cadastro.read()

            if eventos_cadastro == 'salvar_cadastro':
                usuarios = open('usuario.txt', 'a')
                senhas = open('senhas.txt', 'a')
                if valores_cadastro['usuario_cadastro'] == '' or valores_cadastro['senha_cadastro'] == '':
                    print("Informar valor nas duas caixa de texto!")
                else:
                    lista_usuarios = []
                    lista_senhas = []
                    lista_usuarios.append(valores_cadastro['usuario_cadastro'])
                    lista_senhas.append(valores_cadastro['senha_cadastro'])
                    for i in lista_usuarios:
                        usuarios.writelines(i + '\n')
                    for i in lista_senhas:
                        senhas.writelines(i + '\n')
                    janela_cadastro['mensagem'].update('Usuario cadastrado com sucesso!')
                    sg.Window.close(janela_cadastro)
                    break
            if eventos_cadastro == sg.WINDOW_CLOSED:
                break




    elif eventos == 'salvar':  # Clicou em botao LOGIN
        dados = open('dados.txt', 'a')
        usuarios = open('usuario.txt', 'r')
        senhas = open('senhas.txt', 'r')
        lista_usuarios = []
        lista_senhas = []
        for i in usuarios:
            lista_usuarios.append(i)
        for i in senhas:
            lista_senhas.append(i)
        tamanho_usuarios = len(lista_usuarios)
        for i in range(tamanho_usuarios):
            if lista_usuarios[i].replace('\n', '') == valores['usuario'] and lista_senhas[i].replace('\n', '') == \
                    valores['senha']:

                print("Login feito com sucesso!")
                janela['mensagem'].update("Login feito com sucesso!")
                sg.Window.close(janela)
                # janela
                janela_principal = sg.Window('Tela de Cadastro', layout_principal, element_justification='c')
                # ler os eventos
                while True:
                    eventos_principal, valores_principal = janela_principal.read()
                    if eventos_principal == 'Salvar':
                        print('Dados salvos')
                        # dados.writelines(str(valores_principal))
                        cont += 1
                        continue
                    if eventos_principal == 'Parar' or layout_principal:
                        eventos = sg.WINDOW_CLOSED
                        print('Programa encerrado')
                        break
                break

            else:
                janela['mensagem'].update("Usuario ou Senha incorreta!")
                print('teste')

    if eventos == sg.WINDOW_CLOSED:
        print('Programa encerrado')
        break