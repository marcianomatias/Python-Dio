#Herança simples

class Veiculo:
    def __init__(self, cor, placa, numeros_rodas):
        self.cor = cor
        self.placa = placa
        self.numeros_rodas = numeros_rodas
    def ligar_motor(self):
        print("ligando o motor!")
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
class Motocicleta(Veiculo):
    pass
class Carro(Veiculo):
    pass
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numeros_rodas, carga):
        super().__init__(cor,placa,numeros_rodas)
        self.carga = carga
    def esta_carregado(self):
        print(f"{'Estou com carga' if  self.carga else 'Não estou carregado'} para o Rio de Janeiro!")

moto = Motocicleta("preta", "ABC-1C23",2)
print(moto.placa)
moto.ligar_motor()
print("="*100)
carro = Carro("Branco", "AXC-1C23",4)
carro.ligar_motor()
print(carro.numeros_rodas)
print("="*100)
caminhao = Caminhao("Branco", "ACA-1C22",12, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print("="*100)
print(carro)
print(moto)
print(caminhao)

