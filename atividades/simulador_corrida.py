from abc import ABC, abstractmethod


class Veiculo(ABC):

    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass


class Carro(Veiculo):

    def acelerar(self):
        print(f"O carro {self.modelo} acelerou rapidamente!")


class Moto(Veiculo):

    def acelerar(self):
        print(f"A moto {self.modelo} acelerou com muita velocidade!")


class Caminhao(Veiculo):

    def acelerar(self):
        print(f"O caminhão {self.modelo} acelerou lentamente, devido ao seu peso!")


class CarroEletrico(Veiculo):

    def acelerar(self):
        print(f"O carro elétrico {self.modelo} acelerou silenciosamente!")


pista_de_corrida = [
    Carro("Toyota Corolla"),
    Moto("Honda CB 500"),
    Caminhao("Volvo FH"),
    CarroEletrico("Tesla Model 3")
]


for veiculo in pista_de_corrida:
    veiculo.acelerar()