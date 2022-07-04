# lista = []
# while True:
#     while True:
#         n = input('digite numeros, quando quiser parar digite s: ')
#         if n == 's':
#             break
#         lista.append(n)
#     print(lista)
#     lista.sort()
#     print(lista)
#     lista.sort(reverse=True)
#     print(lista)
#     lista = list(map(int, lista))
#     soma = sum(lista)
#     print(soma)
#     print(f'{sum(lista) / len(lista)}')
#     if n == 's':
#         break



# lista = []
# while True:
#     while True:
#         n = str(input('digite os nomes aqui, quando quiser parar digite stop: '))
#         if n == 'stop':
#             break
#         lista.append(n)
#     print(lista)
#     lista.sort()
#     print(lista)
#     lista.sort(reverse=True)
#     print(lista)
#     print(len(lista))
#     print(lista.count('Carlos'))
#     break


#
# lista = []
# listaInt = 0
# listabool = 0
# listafloat = 0
# listaStr = 0
#
# while True:
#     while True:
#         lista_add = input("escreva qualquer coisa, se quiser parar digite 0: ")
#         if lista_add == "0":
#             break
#         lista.append(lista_add)
#
#     for i in range(len(lista)):
#         try:
#             lista[i] = int(lista[i])
#             listaInt += 1
#         except:
#             try:
#                 lista[i] = float(lista[i])
#                 listafloat += 1
#             except:
#                 try:
#                     if lista[i] == 'True' or lista[i] == 'False':
#                         listabool += 1
#                     else:
#                         listaStr += 1
#                 except:
#                     print('...')
#                     break
#     lista.reverse()
#     print(lista)
#     print(listaInt)
#     print(listabool)
#     print(listaStr)
#     print(listafloat)






