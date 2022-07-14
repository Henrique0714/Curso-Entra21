# class Coca:
#     # cor, porta, marca, modelo, ano
#     def __init__(self, altura, diametro, volume, material, cor, rotulo):
#         self.altura = altura
#         self.diametro = diametro
#         self.volume = volume
#         self.material = material
#         self.cor = cor
#         self.rotulo = rotulo
#
#     def __repr__(self):
#         return repr(f'{self.altura}- {self.diametro} - {self.volume} - {self.cor} - {self.rotulo} - {self.material}')
#
#     def abrir(self):
#         print(f' pra {self.cor}')
#
#     def beber(self):
#         print(f'GLUB GLUB pra {self.cor}')
#
#     def esvaziar(self):
#         print(f'XIIIIIIII pro {self.cor}')
#
#     def amassar (self):
#         print(f'CLAC CLAC pra {self.cor}')
#
#     def descartar(self):
#         print(f'LIXOOO pra {self.cor}')
#
#     def retirar(self):
#         print(f'SHAKEEEE pra {self.cor}')
#
# #Instância
# c1 = Coca(10, 5, 350,'alumineo', 'preto', 'se beber não case')
# c2 = Coca(12, 6, 450,'alumineo', 'vermelho', 'se beber não case')
#
# print(c2)


# class Bola:
#     def __init__(self, cor, circunferencia, material):
#         self.cor = cor
#         self.circunferencia = circunferencia
#         self.material = material
#
#     def __repr__(self):
#         return(f'{self.cor} - {self.circunferencia} - {self.material}')
#
#     def trocacor(self, novacor):
#         if self.cor:
#             self.cor = novacor
#
#
#     def mostracor(self):
#         print(self.cor)
#
#
#
# b = Bola('Amarelo', 30, 'coro')
# print(b.cor)
# b.trocacor(input('digite sua cor: '))
# b.mostracor()


# class Quadrado:
#     def __init__(self, TDL):
#         self.TDL = TDL
#
#
#     def MDL(self, novolado):
#         self.TDL = novolado
#
#     def area(self):
#         area = self.TDL**2
#         print(area)
#
#
# t = Quadrado(25)
# print(t.TDL)
# t.MDL(int(input('Digite o tamanho do seu lado: ')))
# print(t.TDL)
# t.area()


# class Retangulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
#
#     def mudar_lados(self, novabase, novotamanho):
#         self.base = novabase
#         self.tamanho = novotamanho
#
#     def valordoslados(self):
#         print(f'{self.base} é a nova base')
#         print(f'{self.tamanho} é o novo tamanho')
#
#     def area(self):
#         return self.base * self.tamanho
#
#     def perimeter(self):
#         return (self.base * 2) + (self.tamanho * 2)
#
#
# rec = Retangulo(int(input('escreva o tamanho da base: ')), int(input('escrava o tamanho da base: ')))
# rec.mudar_lados(10, 10)
# print(rec.area())
# size_floors = 2
# floor_quantity = rec.area() / size_floors
# print(floor_quantity)


# class Bomba:
#     def __init__(self, tipo, valor, qtd, bombinha):
#         self.tipo = tipo
#         self.valor = valor
#         self.qtd = qtd
#         self.bombinha = bombinha
#
#     def abastecerL(self, quanto):
#
#         if self.abastecerL:
#             self.qtd = quanto
#             if quanto <= self.bombinha:
#                 print(f'O valor a pagar é {quanto*self.valor} em {self.tipo}')
#             else:
#                 print('O posto não tem combustível suficiente')
#             pass
#
#     def abastecerV(self, preco):
#         if self.abastecerL:
#             self.qtd = preco
#             print(f'Você vai colocar {float(preco/self.valor):.2f} litros de {self.tipo}')
#             pass
#
#     def alterarV(self, novovalor):
#         self.valor = novovalor
#         print(f'O valor da gasolina agora é de R${self.valor}')
#         pass
#
#     def alterarC(self, tipoDeC):
#         self.tipo = tipoDeC
#         print(f'O tipo de gasolina agora é {self.tipo}')
#         pass
#     def alterarB(self, novaqtd):
#         self.bombinha = novaqtd
#         print(f'Agora restam {novaqtd} litros na bomba')
#
#
#
#
# gasosa = Bomba('Aditivada', 4, 0, 300)
# gasosa.alterarC(input('Qual o novo tipo de gasolina?'))
# gasosa.abastecerV(float(input('Quanto você quer abastecer em reais?')))
# gasosa.abastecerL(float(input('Quantos litros você quer abastecer?')))
# gasosa.alterarV(int(input('Qual o novo valor da gasolina?')))
# gasosa.alterarC(input('Qual o novo tipo de gasolina?'))


class Carro:
    def __init__(self, consumo, tanquecheio=50):
        self.__consumo = consumo
        self.__tanquecheio = tanquecheio
        self.__quantidadecheia = 0

    def add_gas(self, litros):
        self.__quantidadecheia += litros

    def verify_fuel(self):
        print(f'voce tem {self.__quantidadecheia} litros')

    def ride(self, distance):
        liter = distance / self.__consumo
        if liter > self.__consumo:
            print(f'não tem gasolina suficiente')
        else:
            self.__quantidadecheia -= liter
            print(f'a viagem foi ferrada!')


ferrari = Carro(15)
ferrari.add_gas(50)
ferrari.ride(100)
ferrari.verify_fuel()




