from account import *
from os import system as ss

lock = False #Obriga o cliente a fazer o cadastro primeiro.

while True: #Menu
    opt = input("=================BANCO=================\n1. CADASTRAR\n2. SALDO\n3. SAQUE\n4. DEPÓSITO\n5. ALTERAR SENHA\n0. SAIR\n\nESCOLHA: ")


    if opt == "1": #Cadastro


        try:
            ss("cls")
            name = input("NOME: ")
            ss("cls")
            cpf = int(input("CPF: "))
            ss("cls")
            passw = input("SENHA: ")
            bal = 0


        except ValueError:
            ss("cls")
            print("DIGITE AS INFORMAÇÕES CORRETAMENTE.")
            ss("pause")
            ss("cls")


        else:
            ss("cls")
            account = Account(name,bal,cpf,passw)
            lock = True
            print("CADASTRO EFETUADO COM SUCESSO!")
            ss("pause")
            ss("cls")


    elif opt == "2": #Saldo


        if lock == True:
            ss("cls")
            passw = input("INSIRA A SENHA: ")
            ss("cls")
            account.extract(passw)
            ss("pause")
            ss("cls")


        else:
            ss("cls")
            print("VOCÊ NÃO POSSUI CONTA.")
            ss("pause")
            ss("cls")


    elif opt == "3": #Saque


        if lock == True:


            try:
                ss("cls")
                value = float(input("VALOR A SER SACADO: "))
                ss("cls")
                passw = input("INSIRA SUA SENHA: ")
            

            except ValueError:
                ss("cls")
                print("DIGITE SOMENTE NÚMEROS QUANDO FOR SACAR UM VALOR.")
                ss("pause")
                ss("cls")


            else:
                ss("cls")
                account.withdraw(value,passw)
                ss("pause")
                ss("cls")


        else:
            ss("cls")
            print("VOCÊ NÃO POSSUI CONTA.")
            ss("pause")
            ss("cls")


    elif opt == "4": #Deposito


        if lock == True:


            try:
                ss("cls")
                value = float(input("VALOR A SER ADICIONADO: "))


            except ValueError:
                ss("cls")
                print("DIGITE SOMENTE NÚMEROS QUANDO FOR DEPOSITAR UM VALOR.")
                ss("pause")
                ss("cls")

            else:
                ss("cls")
                account.deposit(value)
                ss("pause")
                ss("cls")


        else:
            ss("cls")
            print("VOCÊ NÃO POSSUI CONTA.")
            ss("pause")
            ss("cls")


    elif opt =="5": #Trocar senha


        if lock == True:
            ss("cls")
            passw = input("SENHA: ")
            ss("cls")
            newpass = input("NOVA SENHA: ")
            ss("cls")
            account.pass_change(passw,newpass)
            ss("pause")
            ss("cls")


        else:
            ss("cls")
            print("VOCÊ NÃO POSSUI CONTA.")
            ss("pause")
            ss("cls")


    elif opt == "0": #Sair
        ss("cls")
        print("OBRIGADO POR UTILIZAR NOSSO BANCO.")
        break


    else: #No caso de opções inexistentes.
        ss("cls")
        print("OPÇÃO INEXISTENTE.")
        ss("pause")
        ss("cls")