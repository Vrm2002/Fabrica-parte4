import os
agenda={}
while True:
    try:
        opt=int(input("MENU DA AGENDA===================\n\n1. Registrar CPF\n2. Consultar CPF\n\nESCOLHA: "))

    except ValueError:
        os.system("cls")
        print("Digite somente 1 ou 2. Não digite letras ou outros algarismos.")
        os.system("pause")
        os.system("cls")
    
    except:
        os.system("cls")
        print("Erro desconhecido.")
        os.system("pause")
        os.system("cls")
    
    else:
        os.system("cls")
        if opt==1:
            try:
                cpf=int(input("CPF: "))
                nome=input("Nome: ")
                idade=int(input("Idade: "))
                fone=int(input("Telefone: "))

            except ValueError:
                os.system("cls")
                print("Erro! Você digitou algo errado.")
                os.system("pause")
                os.system("cls")

            except:
                os.system("cls")
                print("Erro desconhecido!")
                os.system("pause")
                os.system("cls")

            else:
                os.system("cls")
                agenda={cpf:[nome,idade,fone]}

        elif opt==2:
            try:
                cpfkey=int(input("Digite o CPF a ser consultado: "))

            except ValueError:
                os.system("cls")
                print("Erro! Digite somente números!")
                os.system("pause")
                os.system("cls")
            
            except:
                os.system("cls")
                print("Erro desconhecido.")
                os.system("pause")
                os.system("cls")

            else:
                os.system("cls")
                if cpfkey in agenda:
                    cpfdigit=cpfkey
                    cpfkey=agenda.get(cpfkey)
                    print("Nome: {:s}\nIdade: {:d}\nTelefone: {:d}\nCPF: {:d}".format(cpfkey[0],cpfkey[1],cpfkey[2],cpfdigit))
                    os.system("pause")
                    os.system("cls")
                else:
                    print("CPF inexistente.")
                    os.system("pause")
                    os.system("cls")