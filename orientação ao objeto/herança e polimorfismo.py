# class Veiculo:
#     def __init__(self, cor, lugares, qnt_pneus, tipo_motor, valor, ano, marca, modelo):
#         self.cor = cor
#         self.qnt_pneus = qnt_pneus
#         self.valor = valor
#         self.ano = ano
#         self.marca = marca
#         self.modelo = modelo
#         self.tipo_motor = tipo_motor
#         self.lugares = lugares
#
#     def acelerar(self):
#         print('Acelerou')
#
#     def frear(self):
#         print('Freou')
#
#     def ligar(self):
#         print('Ligou')
#
#     def desligar(self):
#         print('Desligou')
#
#
# class Moto(Veiculo):
#     def __init__(self, cor, lugares, qnt_pneus, tipo_motor, valor, ano, marca, modelo, empinada=False):
#         super().__init__(cor, lugares, qnt_pneus, tipo_motor, valor, ano, marca, modelo)
#         self.empinada = empinada
#
#     def empinar(self):
#         if self.empinada:
#             print('ja esta empinada')
#         else:
#             print('Impinaaaa')
#             self.empinada = True
#
#     def desempinar(self):
#         self.empinada = False
#
#
# m1 = Moto('Azul', 2, 2, '125C', 17000, 2022, 'Honda', 'CG-125', True)
#
# m1.empinar()
#
#
# class Carro(Veiculo):
#     def __init__(self, cor, lugares, qnt_pneus, tipo_motor, valor, ano, marca, modelo, porta, janela):
#         super().__init__(cor, lugares, qnt_pneus, tipo_motor, valor, ano, marca, modelo)
#         self.porta = porta
#         self.janela = janela
#
#     def abrirp(self):
#         print('Abriu a porta')
#
#     def abrirj(self):
#         print('Abriu a janela')
#
#
# class Onibus(Carro):
#     def __init__(self, cor, lugares, qnt_pneus, tipo_motor, valor, ano, marca, modelo, porta, janela, escada, catraca):
#         super().__init__(cor, lugares, qnt_pneus, tipo_motor, valor, ano, marca, modelo, porta, janela)
#         self.catraca = catraca
#         self.escada = escada
#
#     def subir(self):
#         print('subiu')
#
#     def passar(self):
#         print('passou')
#
#
# c = Carro('Azul', 4, 4, '180CV', 45000, 2012, 'Chevrolet', 'Celta', 4, 4)
# c.abrirp()
# o = Onibus('Amarelo', 16, 10, '180CV', 200000, 2012, 'Chevrolet', 'busao', 4, 4, 4, 4)
# o.passar()
#

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, patas, chifres, rabos, ossos):
        self.rabos = rabos
        self.ossos = ossos
        self.patas = patas
        self.chifres = chifres

    @abstractmethod
    def andar(self):
        if self.patas > 0:
            print('ele anda')

    def chifrar(self):
        print('chifrudo')

    def rabar(self):
        print('tem rabinho')

    def condicionar(self):
        if self.ossos > 0:
            print('vertebrado')
        else:
            print('invertebrado')


class Humano(Animal):
    def __init__(self, patas, chifres, rabos, ossos, orelha, nariz):
        super().__init__(patas, chifres, rabos, ossos)
        self.orelha = orelha
        self.nariz = nariz

    def andar(self):
        print('andou')

    def ouvir(self):
        print('ouviu')

    def cheirar(self):
        print('cheiro de coco')


class Felino(Animal):
    def __init__(self, patas, chifres, rabos, ossos, dentes, carnivoros):
        super().__init__(patas, chifres, rabos, ossos)
        self.carnivoros = carnivoros
        self.dentes = dentes

    def andar(self):
        print('andou')

    def comer(self):
        print('comeu')

    def morder(self):
        print('mordeu')


class Ave(Animal):
    def __init__(self, patas, chifres, rabos, ossos, penas, voo):
        super().__init__(patas, chifres, rabos, ossos)
        self.voo = voo
        self.penas = penas

    def andar(self):
        print('andou')

    def protejer(self):
        print('ta com peninha')


a1 = Felino(2,0,1,12,12,True)
a1.andar()