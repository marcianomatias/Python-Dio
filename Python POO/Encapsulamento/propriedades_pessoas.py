from datetime import date

class Pessoa:
    def __init__(self, nome, ano_nasc):
        self._nome = nome
        self._ano_nasc = ano_nasc
    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        _ano_atual = date.today().year
        return _ano_atual - self._ano_nasc
pessoa = Pessoa("Marciano", 1977)
print("="*100)
print(f"Nome: {pessoa.nome} sua idade é: {pessoa.idade}")