#Herança Multipla
class Animal:
    def __init__(self, numeros_patas):
        self.numeros_patas = numeros_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
    def __str__(self):
        return self.__class__.__name__
class Aquatico(Animal):
    def __init__(self,  cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
    def __str__(self):
        return 'aquatico 42'
class Cachorro(Mamifero):
    pass
class Gato(Mamifero):
    pass
class FalarMixin:
    def falar(self):
        return ("olá sou um Mixin demto da classe ornitorrinco!")
class Leao(Mamifero):
    pass
class Ornitorrinco(Mamifero, Aquatico, FalarMixin):
    def __init__(self, cor_pelo, **kw):
        #print(Ornitorrinco.__mro__)
        print(Ornitorrinco.mro())
        super().__init__(cor_pelo, **kw)
    def __str__(self):
        return "Ornitorrinco"

gato = Gato(numeros_patas=4, cor_pelo="preto")
print(gato)
ornitorrinco = Ornitorrinco(numeros_patas=4, cor_pelo="castanho", cor_bico="laranja")
print(ornitorrinco)
print(ornitorrinco.falar())