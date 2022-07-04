nome = 'Ricardo'

while True:
    idade = int(input('escreva sua idade: '))
    if idade >= 18:
        print(f'{nome} tem {len(nome)} caracteres e  {idade} anos e faltam {50 - idade} para os 50 anos')
        break
    else:
        continue


