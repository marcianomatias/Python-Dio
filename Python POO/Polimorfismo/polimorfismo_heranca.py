class Passaro:
    def voar(self): pass
class Pardal(Passaro):
    def voar(self): pass
    print("Pardal Voa")
class Avestruz(Passaro):
    def voar(self): pass
    print("Avestruz não Voa")
def plano_de_voo(passaro):
    passaro.voar()
plano_de_voo(Pardal())
plano_de_voo(Avestruz())