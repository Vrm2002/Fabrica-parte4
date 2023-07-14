class Account():
    from os import system as ss


    def __init__(self,name,bal:float,cpf,passw):
        self.name = name
        self.__bal = bal
        self.__cpf = cpf
        self.__passw = passw


    def extract(self,passcon): #Extrato bancário


        if passcon == self.__passw:
            print("========= EXTRATO =========\n{:.2f}R$".format(self.__bal))
        

        else:
            print("SENHA INVÁLIDA!")
    

    def deposit(self,value): #Depósito


        if value > 0:
            self.__bal = self.__bal + value
            print("O VALOR FOI ADICIONADO À SUA CONTA.")
        

        else:
            print("VALOR INVÁLIDO!")
        

    def withdraw(self,value,passcon): #Sacar.


        if passcon == self.__passw:


            if value <= self.__bal and self.__bal > 0:
                self.__bal = self.__bal - value
                print("O VALOR {:.2f} FOI SACADO.".format(value))
            
            
            else:
                print("SALDO INSUFICIENTE!")
        

        else:
            print("SENHA INVÁLIDA!")

        
    def pass_change(self,oldpass,newpass): #Trocar senha.


        if oldpass == self.__passw:
            self.__passw = newpass
            print("SENHA ALTERADA COM SUCESSO.")


        else:
            print("SENHA ANTIGA INVÁLIDA.")