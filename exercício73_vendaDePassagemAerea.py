import os

regist=[]
clients=[]

ticket=[]
ticketlist=[]

airship=[]
shiplist=[]

crew=[]
crewmates=[]
#As listas acima são para armazenar as informações.

while True:
    option=input("BEM VINDO AO SOFTWARE DA EMPRESA AÉREA. ESCOLHA UMA OPÇÃO:\n1- Cadastro de Cliente.\n2- Cadastro de Passagem.\n3- Cadastro de Avião.\n4- Cadastro de Tripulação.\n5- Imprimir Relatório\n0- Sair.\nEscolha uma opção: ")
    test=option.isdigit() #Teste pra saber se a variável está com um digito informado.
    if test==True: #Caso sim.
        option=int(option)
        if option==1: #Cadastro de Cliente.
            print("\nCADASTRO DE CLIENTE ---------------------\n")
            try:
                name=input("Nome: ")
                name2=input("Sobrenome: ")
                rg=int(input("RG: "))
                cpf=int(input("CPF: "))
                adress=input("Bairro, Rua e Número: ")
                phone=int(input("Telefone: "))
                age=int(input("Idade: "))
            except:
                os.system("cls")
                print("Erro!")
                os.system("pause")
                os.system("cls")
            else:
                os.system("cls")
                regist.append(name)
                regist.append(name2)
                regist.append(rg)
                regist.append(cpf)
                regist.append(adress)
                regist.append(phone)
                regist.append(age)
                clients.append(regist)
                os.system("pause")
                os.system("cls")
        elif option==2: #Cadastro de Passagemm.
            print("\nCADASTRO DE PASSAGEM ---------------------")
            try:
                destin=input("Destino: ")
                origin=input("Origem: ")
                duration=float(input("Duração: "))
                ticketval=float(input("Valor da passagem: "))
                discount=(ticketval*0.5)-ticketval
                print("Valor com desconto: {:f}".format(discount))
            except:
                os.system("cls")
                print("Erro!")
                os.system("pause")
                os.system("cls")
            else:
                os.system("cls")
                ticket.append(destin)
                ticket.append(origin)
                ticket.append(duration)
                ticket.append(ticketval)
                ticket.append(discount)
                ticketlist.append(ticket)
                os.system("pause")
                os.system("cls")
        elif option==3: #Cadastro de Avião.
            print("\nCADASTRO DE AVIÃO ---------------------")
            try:
                model=input("Modelo: ")
                year=int(input("Ano: "))
                flight=float(input("Horas de Vôo: "))
                collor=input("Cor: ")
                passanger=int(input("Quantidade de passageiros: "))
            except: 
                os.system("cls")
                print("Erro!")
                os.system("pause")
                os.system("cls")
            else:
                os.system("cls")
                airship.append(model)
                airship.append(year)
                airship.append(flight)
                airship.append(collor)
                airship.append(passanger)
                shiplist.append(airship)
                os.system("pause")
                os.system("cls")
        elif option==4: #Cadastro de tripulação.
            print("\nCADASTRO DE TRIPULAÇÃO ---------------------")
            try:
                name=input("Nome: ")
                office=input("Descrição do Cargo: ")
                age=int(input("Idade: "))
                admission=input("Data de Admissão: ")
                phone=int(input("Telefone: "))
            except:
                os.system("cls")
                print("Erro!")
                os.system("pause")
                os.system("cls")
            else:
                os.system("cls")
                crew.append(name)
                crew.append(office)
                crew.append(age)
                crew.append(admission)
                crew.append(phone)
                crewmates.append(crew)
                os.system("pause")
                os.system("cls")
        elif option==5: #Verificar registro.
            os.system("cls")
            option2=int(input("OBRE O QUE DESEJA IMPRIMIR? ---------------------\n1- Clientes.\n2- Passagens.\n3- Aviões.\n4- Tripulantes.\n0- Sair.\nEscolha: "))
            if option2==1: #Clientes.
                os.system("cls")
                try:
                    index=int(input("Digite o número de cadastro do cliente que você deseja ver: "))
                except:
                    os.system("cls")
                    print("Erro!")
                    os.system("pause")
                    os.system("cls")
                else:
                    os.system("cls")
                    print(clients[index])
                    os.system("pause")
                    os.system("cls")
            elif option2==2: #Passagens.
                os.system("cls")
                try:
                    index=int(input("Digite o número de cadastro da passagem registrada: "))
                except:
                    os.system("cls")
                    print("Erro!")
                    os.system("pause")
                    os.system("cls")
                else:
                    os.system("cls")
                    print(ticketlist[index])
                    os.system("pause")
                    os.system("cls")
            elif option2==3: #Aviões.
                os.system("cls")
                try:
                    index=int(input("Digite o número de cadastro do avião: "))
                except:
                    os.system("cls")
                    print("Erro!")
                    os.system("pause")
                    os.system("cls")
                else:
                    os.system("cls")
                    print(shiplist[index])
                    os.system("pause")
                    os.system("cls")
            elif option2==4: #Tripulantes.
                os.system("cls")
                try:
                    index=int(input("Digite o número de cadastro do tripulante: "))
                except:
                    os.system("cls")
                    print("Erro!")
                    os.system("pause")
                    os.system("cls")
                else:
                    os.system("cls")
                    print(crewmates[index])
                    os.system("pause")
                    os.system("cls") 
        elif option==0: #Sair.
            os.system("cls")
            print("Obrigado por usar o sistema!")
            break
    elif test==False: #Caso não.
        os.system("cls")
        print("Erro! Opção inexistente!")
        os.system("pause")
        os.system("cls")
