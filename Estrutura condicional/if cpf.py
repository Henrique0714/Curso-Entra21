cpf = input('digite seu cpf: ')
estado = cpf[10]
print(estado)

if estado == '0':
    print(' Rio grande do sul')
elif estado == '1':
    print('distrito federal,goias, mato grosso,  mato grosso do sul e tocantins')
elif estado == '2':
    print('Amazonas, Pará, Roraima, Amapá, Acre e Rondônia')
elif estado == '3':
    print('Ceará, Maranhão e Piauí')
elif estado == '4':
    print('Paraíba, Pernambuco, Alagoas e Rio Grande do Norte')
elif estado == '5':
    print('Bahia e Sergipe')
elif estado == '6':
    print('Minas Gerais')
elif estado == '7':
    print('Rio de Janeiro e Espírito Santo')
elif estado == '8':
    print('São Paulo')
elif estado == '9':
    print('Paraná e Santa Catarina')

