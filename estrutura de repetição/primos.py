# Número Primo
#  Criar um código que recebe um número,
#  e diga se ele é primo ou não
# Número primo, tem módulo 0 apenas se dividido por 1 ou
# por ele mesmo.
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31..........PRIMOS
# 4,6,8,9,10,12,14,15,16,18,20,21,22,24...........NÃO PRIMOS

contador = 2
numero = int(input('Digite um número: '))

if numero == 1:
    print('Não é primo')
else:
    while contador < numero:
        if numero % contador == 0:
            print("Não é primo")
            break
        contador += 1
    if contador == numero or numero == 2:
        print('É primo')