class Lata:
    def __init__(self, altura, diametro, volume, material='Alumínio', rotulo='Coca'):
        self.altura = altura
        self.diametro = diametro
        self.volume = volume
        self.material = material
        self.rotulo = rotulo
        self.lacre = True
        self.amassada = False
        self.descartada = False
        self.aberta = False


    def abrir(self):
        if self.aberta:
            print(f'ja esta aberta bocó')
        else:
            print(' Lata foi aberta com sucesso')
            self.aberta = True

    def beber(self, quantidade):
        if not self.aberta:
            print('Lata ainda esta fechada')
        elif quantidade > self.volume:
            print(f'Você bebeu {self.volume}, e ainda faltou {quantidade-self.volume}')
            self.volume = 0
        else:
            self.volume -= quantidade
            print(f'Você bebeu {quantidade}, e na lata ainda resta {self.volume}')

    def esvaziar(self):
        if not self.aberta:
            print('Abre 1 bocó')
        else:
            print('lata vazia')
            self.volume = 0

    def amassar(self):
        if not self.amassada and self.volume==0:
            print('Lata amassada')
        else:
            print('nao da pra amassar')

    def retirar_lacre(self):
        if self.lacre:
            self.lacre = False
            print('Lacre retirado')
        else:
            print('não tinha lacre')

    def descartar(self):
        if self.descartada:
            print('não pode destacar o que ja está descartado')
        if self.amassada:
            print('descartada no lixeiro amarelo')
        else:
            print('primeiro, amassa a lata')




l1 = Lata(12.22, 5.2, 350)
l1.abrir()
l1.beber(300)
l1.esvaziar()
l1.amassar()
l1.retirar_lacre()
l1.amassar()
l1.descartar()

