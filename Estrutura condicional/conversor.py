print(30*'-')
txt = 'selecione como uma opção'
txt = txt.center (30)
print(txt)
print(30*'-')

print('1 - Converter de Celsius para Kelvin')
print('2 - Converter de Celsius para Fahrenheit')
print('3 - Converter de Kelvin para Celsius')
print('4- Converter de Kelvin para Fahrenheit')
print('5- Converter de Fahrenheit para Celsius')
print('6 - Converter de Fahrenheit para Kelvin')
n1 = int(input('selecione uma das opções: '))

if n1 == 1:
    print('')
    num1 = int(input('digite seu numero: '))
    print('')
    print(f' de celsius para kelvin é: {num1 + 273,15} K')
if n1 == 2:
    print('')
    num1 = int(input('digite seu numero: '))
    print('')
    print(f' de celsius para fahrenheit é: {num1 * 9/5 +32} F')
if n1 == 3:
    print('')
    num1 = int(input('digite seu numero: '))
    print('')
    print(f' de kelvin para celsius é: {(num1 - 32) * 5/9} F')
if n1 == 4:
    print('')
    num1 = int(input('digite seu numero: '))
    print('')
    print(f' de kelvin para fahrenheit é: {(num1 - 273.15) * 9/5 + 32} F')
if n1 == 5:
    print('')
    num1 = int(input('digite seu numero: '))
    print('')
    print(f' de fahrennheit para celsius é: {(num1 - 32) * 5/9} F')
if n1 == 6:
    print('')
    num1 = int(input('digite seu numero: '))
    print('')
    print(f' de fahrennheit para kelvin é: {(num1 - 32) * 5/9 + 273.15} F')

nome = input('Digite o seu nome: ')
cargo = input('Digite o seu cargo: (1) Professor (2) Coordenador (3) Zelador: ')
salario = float(input('Digite o seu Salário Atual: '))
salario_novo = salario * 1.1
bonificacao = salario_novo * 0.05

if salario_novo < 1999:
    irrf = 0
elif salario_novo < 2967:
    irrf = salario_novo * 0.075
elif salario_novo < 3938:
    irrf = salario_novo * 0.15
elif salario_novo < 4987:
    irrf = salario_novo * 0.225
else:
    irrf = salario_novo * 0.275

salario_liquido = salario_novo - irrf + bonificacao

print(f'COLABORADOR: {nome.upper()}')
if cargo == '1':
    print('CARGO: PROFESSOR')
elif cargo == '2':
    print('CARGO: COORDENADOR')
else:
    print('CARGO: ZELADOR')

print(f'Salário Novo: {salario_novo:.2f}')
print(f'Bonificação: {bonificacao:.2f}')
print(f'IRRF: {irrf:.2f}')
print(f'Salário líquido: {salario_liquido:.2f}')







