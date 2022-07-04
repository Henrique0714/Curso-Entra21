medida1 = int(input('digite a sua medida: '))
medida2 = int(input('digite a sua medida: '))
medida3 = int(input('digite a sua medida: '))

if medida1 > (medida2 + medida3) or medida2 > (medida1 + medida3) or medida3 > (medida2 + medida1):
    print('nao é um triangulo')
elif medida1 == medida2 and medida1 == medida3:
    print('esse traingulo é equilatero')
elif medida1 == medida2 and medida1 != medida3 or medida2 == medida1 and medida2 != medida3 or medida3 == medida1 and medida3 != medida2:
    print('esse triangulo é isoceles')
elif medida1 != medida2 and medida2 != medida3 and medida3 != medida1:
    print('esse triangulo é escaleno')
elif medida1 > (medida2 + medida3) or medida2 > (medida1 + medida3) or medida3 > (medida2 + medida3):
    print('nao é um triangulo')


