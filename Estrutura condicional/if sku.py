
print(50*'-')
print('Sistema de SKUs E21'.center(50))
print(50*'-')
print('1 -Consultar produto pelo código')
print('2 -Cadastrar novo produto')
opcao = input('Qual opção desejada?')

if opcao == '1':
    codigo = input('Digite o código')
    tipo = codigo[0:3]
    if tipo == 'MON':
        tipo_texto = 'Monitor'
    elif tipo == 'TEC':
        tipo_texto = 'Teclado'
    elif tipo == 'MOU':
        tipo_texto = 'Mouse'
    else:
        print('Tipo não existe')
        tipo_texto = '______'

    cor = codigo[4:6]
    if cor == 'PR':
        cor_texto = 'Preto'
    elif cor == 'VM':
        cor_texto = 'Vermelho'
    elif cor == 'BR':
        cor_texto = 'Branco'
    elif cor == 'AZ':
        cor_texto = 'Azul'
    else:
        print('Cor não existe')
        cor_texto = '______'

    material = codigo[7:9]
    if material == 'PP':
        material_texto = 'Polipropileno'
    elif material == 'PE':
        material_texto = 'Polietilino'
    elif material == 'PO':
        material_texto = 'Poliamida'
    else:
        print('Material não existe')
        material_texto = '______'

    geracao = codigo[10:12]
    if geracao == '1G':
        geracao_texto = '1ª Geração'
    elif geracao == '2G':
        geracao_texto = '2ª Geração'
    elif geracao == '3G':
        geracao_texto = '3ª Geração'
    else:
        print('Geração não existe')
        geracao_texto = '______'

    ano = int(codigo[13:17])
    if ano > 2020 and ano < 2025:
        ano_texto = ano
    else:
        ano_texto = '______'

    print(f'{tipo_texto} {cor_texto} {material_texto} {geracao_texto} {ano}')
elif opcao == '2':
    tipo = int(input('Digite o tipo:\n1 - Monitor\n2 - Teclado\n3 - Mouse\n'))
    if tipo == 1:
        tipo_cod = 'MON'
    elif tipo == 2:
        tipo_cod = 'TEC'
    elif tipo == 3:
        tipo_cod = 'MOU'
    else:
        print('tipo inexistente')
        tipo_cod = '___'

    cor = int(input('Digite a cor:\n1 - PRETO\n2 - AZUL\n3 - VERMELHO\n4 - BRANCO'))
    if cor == 1:
        cor_cod = 'BR'
    elif cor == 2:
        cor_cod = 'BR'
    elif cor == 3:
        cor_cod = 'BR'
    elif cor == 4:
        cor_cod = 'BR'
    else:
        print('cor inexistente')
        cor_cod = '__'

    material = int(input('Digite o tipo:\n1 - Polipropileno\n2 - Polietileno\n3 - Poliamida\n'))
    if material == 1:
        material_cod = 'PP'
    elif material == 2:
        material_cod = 'PR'
    elif material == 3:
        material_cod = 'PO'
    else:
        print('material inexistente')
        material_cod = '__'

    geracao = int(input('Digite o tipo:\n1 - 1ª Geração\n2 - 2ª Geração\n3 - 3ª Geração\n'))
    if geracao == 1:
        geracao_cod = '1G'
    elif geracao == 2:
        geracao_cod = '2G'
    elif geracao == 3:
        geracao_cod = '3G'
    else:
        print('geração inexistente')
        geracao_cod = '__'

    ano = int(input('Digite o ano, entre 2020 e 2025:'))
    if ano > 2025 or ano < 2020:
        print('Ano inexistente')
        ano_cod = ''
    else:
        ano_cod = ano

    print(f'{tipo_cod}-{cor_cod}-{material_cod}-{geracao_cod}-{ano_cod}')
else:
    print('Adiós Muchacho')









