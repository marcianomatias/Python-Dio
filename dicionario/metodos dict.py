contatos = {
    "mms@mail.com": {"nome": "Marciano", "telefone": "3333-1234"},
    "maams@mail.com": {"nome": "Marcia", "telefone": "3233-1200"},
    "matias@mail.com": {"nome": "Marcos", "telefone": "3300-1234"},
    "mass@mail.com": {"nome": "Matis", "telefone": "3003-1004"},
}
print("metodo clear")
contatos.clear()
print(contatos.items())
contatos = {
    "mms@mail.com": {"nome": "Marciano", "telefone": "3333-1234"},
}
print("metodo copy")
copia = contatos.copy()
copia["mms@mail.com"] = {"nome": "marte"}
print(copia)
print(contatos.items())
copia["mms@mail.com"] = {"nome": "marte"}
print(copia)
print("metodo fromkeys")
dict.fromkeys(["nome", "telefone"])
print(dict.fromkeys(["nome", "telefone"]))
dict.fromkeys(["nome", "telefone"], "vazio")
print(dict.fromkeys(["nome", "telefone"],"vazio"))


