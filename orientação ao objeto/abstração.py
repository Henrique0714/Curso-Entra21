from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, especie, habitat):
        self.habitat = habitat
        self.especie = especie
        self.nome = nome

    @abstractmethod
    def pedir_comida(self):
        return True

    def comer(self):
        print(f'{self.nome} comeu')

    @classmethod
    def morrer(cls):
        print('morreu')

class Felinos(Animal):
    def __init__(self, nome, especie, habitat, garras, orelhas):
        super().__init__(nome, especie, habitat)
        self.garras = garras
        self.orelhas = orelhas

    def pedir_comida(self):
        print('Miauuu')


gato = Felinos('joão', 'gato', 'mato', True, 2)
gato.pedir_comida()
Animal.morrer()
