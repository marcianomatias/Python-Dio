class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.marticula = numero


    def __str__(self):
        return f'{self.nome} {self.escola} {self.marticula}'

marte = Estudante("Marte", 25467)
maciano = Estudante("Marciano", 74254)

print(marte)
print(maciano)
