import datetime
print("Criando data e hora")
print("Objeto timedelta")

d = datetime.datetime(2023, 7, 19, 13, 45)
print(d)
print("="*100)
print("Adicionado uma semana")
d = d + datetime.timedelta(weeks=1)
print(d)
print("Adicionado duas semana")
d = d + datetime.timedelta(weeks=2)
print(d)
print("="*100)





