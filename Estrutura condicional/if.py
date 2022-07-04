nome = input('digite seu nome: ')
n1 = int(input('digite a nota 1: '))
n2 = int(input('digite a nota 2: '))
n3 = int(input('digite a nota 3: '))
n4 = int(input('digite a nota 4: '))
média = (n1 + n2 + n3 + n4) / (4)

print(média)

if média >= 7:
    print(f'{nome} voce foi aprovado')
elif média >= 5:
    print(f'{nome} voce foi para o exame')
else:
    print(f'{nome} estude mais seu merda')
