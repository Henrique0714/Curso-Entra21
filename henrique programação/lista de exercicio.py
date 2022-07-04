# print(' OPERAÇÃO - SUBISTITUIÇÃO')
# print(50 * '=')
# for i in range(1, 4):
#     print(f'CONTA {i}')
#     n1 = int(input('digite seu número: '))
#     n2 = int(input('digite seu segundo numero: '))
#     print(f'{n1} - {n2} = {n1 - n2}')
#     print(50 * '-')
#     print(50 * '-')



#
# n = int(input('digite seu número: '))
# print(f'numeros impares: ', end= ' ' )
# for i in range(n+1):
#     if i % 2 != 0:
#         print(i, end= ' ')



# women_list = []
# men_list = []
# n = 0
# print("DOUBLE!\n")
# for i in range(3):
#     w = input("type the name of the women: ")
#     women_list.append(w)
#     print("women: ", end=" ")
# print(women_list[0:3])
# print()
# for i in range(3):
#     m = input("type the name of the men: ")
#     men_list.append(m)
# print(men_list[0:3])
# print()
# for i in range(3):
#     print(f"Double{n}: {women_list[i]} e {men_list[i]}")
#     n += 1



# print('TABUADAS!')
# while True:
#     T = input('Deseja ver uma tabuada? digite S para sim ou N para não: ').upper()
#     if T == 'S':
#         n1 = int(input('digite um número: '))
#         for i in range(1, 11):
#             print(f'{n1} x {i} = {n1 * i}')
#     if T == 'N':
#         print('Então pq rodou o código?')
#         break




# print('CADASTRO DE PRODUTOS!!!')
# P = int(input('Quantos produtos você deseja cadastrar ?: '))
# print(70*'=')
# for i in range(P):
#     i = i + 1
#     print(f'PRODUTO {i}')
#     PP = input('digite seu produto: ')
#     PPP = float(input(' digite o preço do produto: '))
#     if P > 0:
#         print(f'Produto: {PP} = {PPP} ')
#         print(70 * '=')

# T_list = []
# while True:
#     T = input('Digite os times, quando quiser parar digite sair : ')
#     if T == 'sair':
#         break
#     T_list.append(T)
#
#
# for i in T_list:
#     for j in T_list:
#         if i == j :
#             continue
#         print(f'{i}[ ] X [ ]{j}')
#
#
#

# times = []
# for i in arquivo:
#     i = i.replace('\n','')
#     times.append(i)

# from random import randint
# times_lista = []
# print('CONFRONTO BRASILEIRÃO:'.center(50))
# print(50 * '_')
# print(50 * '_')
# d = int(input('Digite a quantidade de times: '))
#
# for i in range(d):
#     time = input('Digite o nome de um time:')
#     times_lista.append(time)
# for j in times_lista:
#     for k in times_lista:
#      if j != k:
#       gol1 = randint(0, 5)
#       gol2 = randint(0, 5)
#       print(f'{j} {gol1} x {gol2} {k}')
# bi = 0
# pares = 0
# ímpares = 0
# futuros = 0
# passados = 0
#
# ano = int(input("Digite um ano/Quando quiser para digite 0\nResposta: "))
# while ano > 0:
#
#     print(ano)
#     if ano >= 2022:
#      futuros += 1
#     else:
#      passados += 1
#     if ano % 2 == 0:
#      pares += 1
#     else:
#      ímpares += 1
#     if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#
#      bi +=1
#     ano = int(input("Digite um ano/Quando quiser para digite 0\nResposta: "))
# if ano == 0:
#
#
#     print(f'Total de anos pares:  {pares} ')
#     print(f'Total de anos ímpares:  {ímpares}')
#     print(f'Total de anos futuros:  {futuros} ')
#     print(f'Total de anos passados:  {passados} ')
#     print(f'Total de anos bissextos:  {bi} ')
#
#
#     ano = int(input("Digite um ano...\nResposta: "))






























