# def T(m1, m2, m3):
#     if m1 > m2 + m3 or m2 > m1 + m3 or m3 > m1 + m2:
#         return 'Não é um triângulo'
#     elif m1 == m2 and m1 == m3:
#         return 'Equilátero'
#     elif m1 == m2 or m1 == m3 or m2 == m3:
#         return'Isósceles'
#     else:
#         return 'Escaleno'

# def contar(lis, let):
#     return lis.count(let)

# def Lista(list):
#     return list[::-1]

# def L(num):
#     cont = 0
#     for i in num:
#         cont += 1
#         pass
#     return cont
import random
import time

while True:
    contJ = 0
    contBOT = 0
    for i in range(3):
        Jogo = input('digite Pedra, Papel ou Tesoura: ')
        print('JO...', end='')
        time.sleep(0.5)
        print('KEN...', end='')
        time.sleep(0.5)
        print('PO...', end='')



        def Jogo1():
            if Jogo == 'Pedra' or Jogo == 'pedra':
                return '\nVamos ver o que o oponente escolhe\n'
            elif Jogo == 'Papel' or Jogo == 'papel':
                return '\nVamos ver o que o oponente escolhe\n'
            elif Jogo == 'Tesoura' or Jogo == 'tesoura':
                return '\nVamos ver o que o oponente escolhe\n'


        Jogo_list = ['Pedra', 'Papel', 'Tesoura']
        BOT = random.choice(Jogo_list)


        def ganhador():
            if Jogo == BOT:
                return 'Jogo empatado'
            elif Jogo == 'Pedra' and BOT == 'Papel' or Jogo == 'Papel' and BOT == 'Tesoura' or Jogo == 'Tesoura' and BOT == 'Pedra':
                return 'Você perdeu otário'
            else:
                return 'Você ganhou Lindão(ona)'


        print(f'{Jogo1()}')
        print(f'A escolha do oponente foi {BOT.upper()}!')
        print(f'{ganhador()}! Vamos jogar denovo\n')


