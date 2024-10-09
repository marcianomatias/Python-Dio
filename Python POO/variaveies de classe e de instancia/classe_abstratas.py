from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print('Ligando')
    def desligar(self):
        print('Desligando')
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando ar...')
    def desligar(self):
        print('Desligando ar...')




controle = ControleTv()
controle.ligar()
controle.desligar()
controle = ControleArCondicionado()
controle.ligar()
controle.desligar()