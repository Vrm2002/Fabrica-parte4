class Account():
    from os import system as ss


    def __init__(self,name,bal,cpf,passw):
        self.name = name
        self.__bal = bal
        self.__cpf = cpf
        self.__passw = passw


    def extract(self,passcon):


        if passcon == self.__passw:
            print("========= EXTRATO =========\n{:.2f}R$".format(self.__bal))
        

        else:
            print("SENHA INVÁLIDA!")
    

    def deposit(self,value):


        if value > 0:
            self.__bal = self.__bal + value
        

        else:
            print("VALOR INVÁLIDO!")
        

    def withdraw(self,value):


        if value <= self.__bal:
            self._bal = self._bal - value
        
        
        else:
            print("SALDO INSUFICIENTE!")

        
    def pass_change(self,oldpass,newpass):
        oldpass = input("DIGITE A SENHA ANTERIOR!")


        if oldpass == self.__passw:

