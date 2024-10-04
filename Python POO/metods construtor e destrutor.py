# __init__ é um método construtor ou iniciliador
# __del__ é um método desconstrutor

class Dog:
    def __init__(self, name, color, acordado=True):
        print("Iniciando a classe...")
        self.name = name
        self.color = color
        self.acordado = acordado
    def latir(self):
        print("auauau")
    def __del__(self):
        print("Destruindo a instância!")
#def criar_dog():
    #c = Dog("Luna","prateada", False)
    #print(c.name)
    #print(c.color)
    #print(c.acordado)

c = Dog("Spike", "Black", True)
#print(c.latir())
c.latir()
print("esta latindo!")
del  c
print("esta latindo!")
print("esta latindo!")


#criar_dog()

