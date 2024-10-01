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
print("="*100)
print("metodo get")
contatos = {
    "mms@mail.com": {"nome": "Marciano", "telefone": "3333-1234"},
}
#contatos["chave"] KeyError
print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("mms@mail.com", {}))
print("="*100)
print("metodo items")
print(contatos.items())
print("="*100)
print("metodo Keys")
print(contatos.keys())
print("="*100)
print("metodo pop")
print(contatos.pop("mms@mail.com"))
print(contatos.pop("mms@mail.com", "Não encontrado!"))
print(contatos.pop("mms@mail.com",{}))
print("="*100)
print("metodo popitem")
contatos = {
    "mms@mail.com": {"nome": "Marciano", "telefone": "3333-1234"},
}
print(contatos.popitem())
print("="*100)

print("metodo setdefault")
contato = {"nome": "Marciano", "telefone": "3333-1234"},
#contato.setdefault("nome", "Marciano")
print(contato)
#contato.setdefault("idade", 18)
#print(contato)
print("="*100)
print("metodo update")
contatos = {
    "mms@mail.com": {"nome": "Marciano", "telefone": "3333-1234"},
}
contatos.update({"mms@mail.com", {"nome": "marte"}})
print(contatos)
print("="*100)




