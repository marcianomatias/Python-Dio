import datetime
import pytz
print("Trabalhando com tymezone - fuso horario")
print("Fuso horario de São Paulo")
d = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
print(d)
print("="*100)
print("Fuso horario de Oslo na Europa")
d = datetime.datetime.now(pytz.timezone('Europe/Oslo'))
print(d)
print("="*100)
print("Fuso horario de Boa Vista RR")
d = datetime.datetime.now(pytz.timezone('America/Boa_Vista'))
print(d)
