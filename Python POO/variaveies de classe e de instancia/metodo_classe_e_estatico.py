class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    @classmethod #Método de classe
    def criar_apartir_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

p1 = Pessoa.criar_apartir_nascimento(1977, 2, 27, "Marciano")
print(f"Meu nome é: {p1.nome}, tenho {p1.idade}  anos")

print(Pessoa.maior_idade(25))
print(Pessoa.maior_idade(17))