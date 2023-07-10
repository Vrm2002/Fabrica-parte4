class Conta():


    def __init__(self,agencia,conta,nome,fone,saldo,cpf):
        self.agencia = int(agencia)
        self.conta = int(conta)
        self.nome = nome
        self.fone = int(fone)
        self.saldo = float(saldo)
        self.cpf = int(cpf)

    
    def saque(self,sacar):
        self.saldo = self.saldo - sacar

    
    def deposito(self,depositar):
        self.saldo = self.saldo + depositar
    
    def extrato(self):
        print(self.saldo)