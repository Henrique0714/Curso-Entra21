import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------------------------------------------------
# plt.plot([1,2,3,4], [1,4,9,16]) #(x, y)
# plt.show()

# -----------------------------------------------------------------------------------------------------------------------

# #plot 1:
# x = [0, 1, 2, 3]
# y = [3, 8, 1, 10]
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# #plot 2:
# x = [0, 1, 2, 3]
# y = [10, 20, 30, 40]
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.show()

# -----------------------------------------------------------------------------------------------------------------------
# # pie
# y = [35, 25, 25, 15]
# mylabels =["a", "b", "c", "d"]
# plt.pie(y, labels = mylabels)
# plt.show()
#
# # enphatize
# y = [35, 25, 25, 15]
# mylabels = ["a", "b", "c", "d"]
# myexplode = [0.2, 0, 0, 0] # Aqui se define a distancia que irá ser destacada
# plt.pie(y, labels = mylabels, explode = myexplode)
# plt.show()

# -----------------------------------------------------------------------------------------------------------------------

# 1:
# plt.suptitle("store")
# x = [0, 1, 2, 3]
# y = [3, 8, 1, 10]
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("selling")

# 2:
# x = [0, 1, 2, 3]
# y = [10, 20, 30, 40]
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("orders")
# plt.show()

# -----------------------------------------------------------------------------------------------------------------------

# EX 1
# y = [10, 20, 30, 40]
# x = ['January', 'February', 'March', 'April']
#
# plt.xlabel('MONTHS', color='r', size=11)
# plt.ylabel('PROFIT', color='r', size=11)
# plt.title('MONTHLY BALANCE', color='k', size=20)
# plt.plot(x, y,  linewidth=2.5, color='c')
# plt.legend(['Yield'], loc='upper left')
# plt.grid(color='g', linestyle=':', lw=0.8)
# plt.show()

# EX 2
# mylabels = ['TI 50%', 'Adm 30%', 'Inglês 10%', 'E. Civil 10%']
# y = [50, 30, 10, 10]
# plt.pie(y, labels=mylabels)
# plt.show()

# EX 3
# y = [3, 8, 1]
# x = ['January', 'February', 'March']
#
# plt.xlabel('months', color='y', size=11)
# plt.ylabel('Visitors', color='y', size=11)
# plt.title('Jonas Ex Teacher', color='b', size=15)
# plt.bar(x, y, color='r')
# plt.show()

# EX 4
# y = [3, 8, 1]
# x = ['January', 'February', 'March']
# plt.figure(figsize=(8, 4))
# plt.xlabel('months', color='y', size=11)
# plt.ylabel('Visitors', color='y', size=11)
# plt.title('Jonas Ex Teacher', color='b', size=15)
# plt.barh(x, y, color='r')
# plt.grid(color='g', linestyle=':', lw=0.5)
# plt.show()

# -----------------------------------------------------------------------------------------------------------------------

# print(30*"=")
# print("GRÁFICOS DE MÉDIAS DO SEMESTRE")
# print(30*"=")
# nomes = []
# notas = []
# vezes = int(input("Digite quantas médias serão lançadas: "))
# for i in range(vezes):
#     nomes.append(input("Digite o nome do aluno(a): "))
#     notas.append(float(input("Digite a média: ")))
# if len(notas) == len(nomes):
#     x = np.arange(len(notas))
#     colors=[]
#     for i in range(len(notas)):
#         if notas[i]>=7:
#             colors.insert(i, "green")
#         else:
#             colors.insert(i, "red")
#     fig, ax = plt.subplots()
#     ax.bar(x, notas, alpha=0.5, color=colors)
#     plt.axhline(y = 7, color = 'k', linestyle = '-')
#     plt.suptitle("Média dos alunos")
#     plt.title("Média baseada nas notas do decorrente semestre")
#     plt.xticks(x, nomes)
#     plt.show()
# else:
#     print("Verifique os seus dados")

# -----------------------------------------------------------------------------------------------------------------------

# from matplotlib.animation import FuncAnimation
# fig, ax = plt.subplots(figsize=(5, 3))
# ax.set(xlim=(-3, 3), ylim=(-1, 1))
# x = np.linspace(-3, 3, 91)
# t = np.linspace(1, 25, 30)
# X2, T2 = np.meshgrid(x, t)
# sinT2 = np.sin(2*np.pi*T2/T2.max())
# F = 0.9*sinT2*np.sinc(X2*(1 + sinT2))
# line = ax.plot(x, F[0, :], color='k', lw=2)[0]
#
# def animate(i):
#     line.set_ydata(F[i, :])
# anim = FuncAnimation(
# fig, animate, interval=100, frames=len(t)-1)
# plt.draw()
# plt.show()

# y = [5, 20, 10]
# x = ['Aprendizado Mínimo', 'Aprendizado Médio', 'Aprendizado Máximo']
#
# plt.xlabel('mínimo aprendizado', color='g', size=11)
# plt.ylabel('alunos', color='g', size=11)
# plt.title('Gráfico de Alunos', color='r', size=15)
# plt.bar(x, y, color='gray')
# plt.grid(color='gray', linestyle=':', lw=0.5)
# plt.show()

# plt.figure(figsize=(7, 7))
# plt.plot(['January', 'February', 'March', 'April', 'Maio'], [10000, 20000, 30000, 2000, 12000], [20000, 10000, 40000, 5000, 8500])
# plt.title('Gráfico de lucro por mês das empresas Jonas e reiter', size=12, color='r')
# plt.legend(["Jonas", "Reiter"], loc="upper right")
# plt.xlabel('meses', color='r', size=10)
# plt.ylabel('lucro', color='r', size=10)
# plt.grid(axis='y', color='gray', linestyle=':', lw=0.5)
# plt.show()


# plt.figure(figsize=(7, 7))
# mylabels = ['pão', 'bebidas', 'balas', 'salgados', 'bolos e cucas', 'café']
# y = [30, 20, 10, 20, 15, 5]
# myexplode = [0.2, 0, 0, 0, 0, 0]
# plt.title('Padaria seu Jonas', size=12, color='r')
# plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
# plt.show()


