#classe para um veículo
class Veiculo:
    # cor, porta, marca, modelo, ano
    def __init__(self, cor, porta, marca, modelo, ano):
        self.cor = cor
        self.porta = porta
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __repr__(self):
        return repr(f'{self.marca}- {self.modelo} - {self.porta} - {self.cor} - {self.ano}')

    def ligar(self):
        print(f'WRUMM WRUMMM pro {self.modelo}')

    def desligar(self):
        print(f'ACABOU O WRUMM WRUMM pro {self.modelo}')

#Instância
v1 = Veiculo('Branco', 4, 'Audi', ' A4', 2005)
v2 = Veiculo('Preta', 2, 'volkswagem', 'Gol Chaleira', 1992)


veiculos = []

for _ in range(2):
    cor = input('Digite a cor: ')
    porta = input('Digite a qtd de portas: ')
    marca= input('Digite a marca: ')
    modelo = input('Digite o modelo: ')
    ano = input('Digite o ano: ')
    cadastro = Veiculo(cor, porta, marca, modelo, ano)
    veiculos.append(cadastro)

print(repr(veiculos))
