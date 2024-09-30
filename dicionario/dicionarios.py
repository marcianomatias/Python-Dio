#Criaçõa e acesso aos dados
pessoa = {"nome":"Marciano","idade":47}
print(pessoa)
pessoa = dict(nome="Marciano",idade=47)
print(pessoa)
pessoa["telefone"] = "3333-1234"
print(pessoa)
print(pessoa["telefone"])
print(pessoa["idade"])
print(pessoa["nome"])

contatos = {
    "mms@mail.com": {"nome": "Marciano", "telefone": "3333-1234"},
    "maams@mail.com": {"nome": "Marcia", "telefone": "3233-1200"},
    "matias@mail.com": {"nome": "Marcos", "telefone": "3300-1234"},
    "mass@mail.com": {"nome": "Matis", "telefone": "3003-1004"},
}
print(contatos)
print("contatos")
telefone = contatos["mms@mail.com"]["telefone"]
print(telefone)
print("Primeira interação")
for chave in contatos:
    print(chave, contatos[chave])
print("="*100)
print("Segunda interação com items")
for chave, valor in contatos.items():
    print(chave, valor)