# Público =  pode ser accessado fora  da classe
# Privado = só pode ser accessado pela  da classe inicica com _(underline)

class Conta:
    def __init__(self,nro_agencia ,saldo=0):
        self.nro_agencia = nro_agencia
        self._saldo = saldo #Privado

    def depositar(self, valor): #publico
        self._saldo += valor
    def sacar(self, valor): #publico
        self._saldo -= valor
    def mostra_saldo(self):
        return self._saldo
conta = Conta("0001", 100)
conta.depositar(100)
print(f"Seu numero de agencia: {conta.nro_agencia}")
#conta.sacar(10)
print(f"Seu saldo após o saque  {conta.sacar(10)} e: {conta.mostra_saldo()}")
