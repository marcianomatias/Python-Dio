class Passaro:
    def voar(self):
        print("Voando...")
class Pardal(Passaro):
    def voar(self):
        super().voar()
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa!")
def plano_voo(obj): #poliformismo
    obj.voar()

p1 = Pardal()


plano_voo(p1)
plano_voo(Avestruz()) # fazendo chamada sem variavel