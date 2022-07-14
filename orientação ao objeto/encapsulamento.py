class Conta:
    def __init__(self, agencia, conta, saldo = 0.0 ):
        self.agencia = agencia
        self.conta = conta
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor
        self.__mensagem()


    def versaldo(self):
        print(self.__saldo)


    def __mensagem(self):
        print(f'Bom dia, seu depósito foi feito')

c1 = Conta(3365, '1234-5')
c1.depositar(200)



