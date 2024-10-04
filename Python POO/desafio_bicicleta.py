
class Bike:
    def __init__(self, color, model, year, value, aro=18):
        self.color = color # atributo da classe
        self.model = model
        self.year = year
        self.value = value
        self.aro = aro
        #para definir um metodos
    def buzinar(self):
        print("Plim, plim..")
    def stop(self):
        print("Stopping the bike!")
        print("Stop running!")
    def run(self):
        print("Bike running.....!")
    def trocar_marcha(self, nro_marcha):
        print("changing gear")
        _self = self

        #def _trocar_marcha():
            #if nro_marcha > _self.marcha:
                #print("changing gear")
            #else:
               # print("Unable to change gear")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bike("red","caloi",2022,600)

b1.run()
b1.buzinar()
b1.stop()

print(f"Bike: {b1.model, b1.color, b1.year, b1.value}")


b2 = Bike("blue","monark",1970,1600)
print(b2)
Bike.buzinar(print(f"Bike 2 em uso: {b2}"))
Bike.stop(b2)
Bike.run(b2)
print(b2.color)
print(b2.year)
