from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print('Ligando')
    def desligar(self):
        print('Desligando')

    @property
    def marca(self):
        return "LG"





class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando ar...')
    def desligar(self):
        print('Desligando ar...')

    @property
    def marca(self):
        return "Samsung"




controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)
controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
