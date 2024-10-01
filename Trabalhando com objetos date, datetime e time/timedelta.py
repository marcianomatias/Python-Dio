from datetime import datetime, timedelta, date, time

tipo_carro = "G"# P,M,G
tempo_pequeno = 30
tempo_medio = 45
tempo_grade = 60
data_atual = datetime.now()
if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou as : {data_atual} e ficará pronto as: {data_estimada}')
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou as : {data_atual} e ficará pronto as: {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grade)
    print(f'O carro chegou as : {data_atual} e ficará pronto as: {data_estimada}')
print("="*100)
print("decrementa um dia ou quantos dias quiser")
print(date.today() - timedelta(days=1))
print("=" * 100)
print("decrementa uma hora ou quantas horas quiser")
result = datetime(2024, 7, 25, 10, 10, 20) - timedelta(hours=1)
print(result.time())
print("=" * 100)
print("Pegando a data e hora local do momento em execução")
print(datetime.now().date())
print(datetime.now().time())
