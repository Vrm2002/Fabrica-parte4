from os import system as ss
from Conta import *

lock = True #Cadeado caso o usuário não tenha conta.


while True:


    try: #Menu
        opt = int(input("BANCO---------------------------------------------------------\n1. CADASTRO\n2. SAQUE\n3. DEPOSITO\n4. EXTRATO\n0. SAIR\n\nESCOLHA: "))
    
    except ValueError:
        ss("cls")
        print("Digite somente números para as opções.")
        ss("pause")
        ss("cls")
    
    except:
        ss("cls")
        print("Erro desconhecido. Tente novamente.")
        ss("pause")
        ss("cls")
    
    else:


        if opt == 1: #Cadastro.


            try:
                ss("cls")
                agencia = int(input("Digite os números de sua agência sem pontuações: "))
                ss("cls")
                conta = int(input("Digite os números da sua conta sem pontuações: "))
                ss("cls")
                nome = input("Digite o nome do titular: ")
                ss("cls")
                fone = int(input("Digite o telefone: "))
                ss("cls")
                saldo = 0
                cpf = int(input("CPF do titular: "))
            
            except ValueError:
                ss("cls")
                print("Erro nas credenciais.")
                ss("pause")
                ss("cls")
            
            except:
                ss("cls")
                print("Erro desconhecido.")
                ss("pause")
                ss("cls")
            
            else:
                ss("cls")
                account = Conta(agencia,conta,nome,fone,saldo,cpf)
                lock = False
                print("Conta registrada com sucesso!")
                ss("pause")
                ss("cls")
        

        elif opt == 2: #Saque.


            if lock == False:

                
                try:
                    ss("cls")
                    saque = float(input("Digite o valor a ser sacado: "))

                except ValueError:
                    ss("cls")
                    print("Erro no valor digitado. Digite somente números.")
                    ss("pause")
                    ss("cls")
                
                except:
                    ss("cls")
                    print("Erro desconhecido.")
                    ss("pause")
                    ss("cls")

                else:


                    if saque > account.saldo:
                        ss("cls")
                        print("Saldo insuficiente.")
                        ss("pause")
                        ss("cls")
                    
                    else:
                        ss("cls")
                        account.saque(saque)
                        print("Valor retirado com sucesso.")
                        ss("pause")
                        ss("cls")


            else:
                ss("cls")
                print("Você não possui cadastro.")
                ss("pause")
                ss("cls")


        elif opt == 3: #Deposito


            if lock == False:


                try:
                    ss("cls")
                    deposito = float(input("Digite o valor a ser depositado: "))

                except ValueError:
                    ss("cls")
                    print("Erro no valor digitado. Digite somente números.")
                    ss("pause")
                    ss("cls")
                
                except:
                    ss("cls")
                    print("Erro desconhecido.")
                    ss("pause")
                    ss("cls")
                
                else:


                    if deposito <= 0:
                        ss("cls")
                        print("Você não está depositando nada.")
                        ss("pause")
                        ss("cls")

                    else:
                        ss("cls")
                        account.deposito(deposito)
                        print("Valor adicionado com sucesso.")
                        ss("pause")
                        ss("cls")


            else:
                ss("cls")
                print("Você não possui cadastro.")
                ss("pause")
                ss("cls")


        elif opt == 4: #Extrato


            if lock == False:
                ss("cls")
                print("Saldo----------------- ")
                account.extrato()
                ss("pause")
                ss("cls")
            

            else:
                ss("cls")
                print("Você não possui cadastro.")
                ss("pause")
                ss("cls")
        

        elif opt == 0: #Sair.
            ss("cls")
            print("Obrigado por utilizar nosso banco.")
            break


        else:
            ss("cls")
            print("Opção inexistente.")
            ss("pause")
            ss("cls")