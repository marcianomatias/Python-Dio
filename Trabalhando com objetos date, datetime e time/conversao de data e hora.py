from datetime import datetime

print("Formatação de data e hora")
d = datetime.now()

# Imprimindo a data e hora no formato desejado
print(d.strftime("Hoje é o dia %d/%m/%Y às %H:%M"))
print(d.strftime("Hoje é o dia %d/%m/%Y às %H:%M:%S"))

print("="*100)
print("Convertendo string para datetime")

# Definindo a string de data e hora
date_str = "20/09/2024 15:30"

# Convertendo a string para um objeto datetime usando strptime
d = datetime.strptime(date_str, "%d/%m/%Y %H:%M")

# Imprimindo o resultado
print(d)

print("="*100)
print("Métodos strftime")
data_hora_atual = datetime.now()
data_hora_srt = "09/20/2024 15:30"
mascara_ptbr = '%d.%m.%Y %H:%M %a'
mascara_en = '%m/%d/%Y %H:%M'
print(f"Formato internacional => {data_hora_srt}")
print("Formato de data e hora em Pt-BR")
print(data_hora_atual.strftime(mascara_ptbr))
print("="*100)
print("Método strptime")
data_convertida = datetime.strptime(data_hora_srt, mascara_en)
print(data_convertida)
print(type(data_convertida))