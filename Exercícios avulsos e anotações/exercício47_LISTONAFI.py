cont=0
start=True
while True:
    opt=int(input("------------------BEM VINDO AO REGISTRO DO ALUNO. O QUE VOCÊ DESEJA?-------------------\n1. Registrar um Aluno\n2. Consultar Registro\n3. Deletar Registro\n4. Sair"))

    while opt==1: #Registro de aluno.
        name=[]
        secondname=[]
        adress=[]
        slam=[]
        city=[]
        state=[]
        country=[]
        phone=[]
        cpf=[]
        wheight=[]
        height=[]
        age=[]
        card=[]
        email=[]
        cep=[]
        not1=[]
        not2=[]
        not3=[]
        not4=[]
        avrg=[]
        year=[]
        clas=[]
        sex=[]
        collor=[]
        regist=[] #Tudo acima são listas.

        namevar=input("Nome: ")
        secondnamevar=input("Sobrenome: ")
        adressvar=input("Rua e Número da Casa: ")
        slamvar=input("Bairro: ")
        cityvar=input("Cidade: ")
        statevar=input("Estado: ")
        countryvar=input("País: ")
        phonevar=int(input("Telefone: "))
        cpfvar=input("CPF: ")
        wheightvar=float(input("Peso: "))
        heightvar=float(input("Altura: "))
        agevar=int(input("Idade: "))
        cardvar=int(input("Cartão: "))
        emailvar=input("Email: ")
        cepvar=int(input("CEP: "))
        not1var=float(input("Nota do primeiro bimestre: "))
        not2var=float(input("Nota do segundo bimestre: "))
        not3var=float(input("Nota do terceiro bimestre: "))
        not4var=float(input("Nota do quarto bimestre: "))
        avrgvar=(not1var+not2var+not3var+not4var)/4
        yearvar=int(input("Série: "))
        clasvar=input("Classe: ")
        sexvar=input("Sexo M/F: ")
        sexvar=sexvar.capitalize()
        collorvar=input("Cor de Pele: ")
        cont=cont+1
        registvar=cont #Tudo acima são variáveis de informações. Que são adicionadas futuramente em listas. E o contador no final é para a matrícula.

        name.append(namevar)
        secondname.append(secondnamevar)
        adress.append(adressvar)
        slam.append(slamvar)
        city.append(cityvar)
        state.append(statevar)
        country.append(countryvar)
        phone.append(phonevar)
        cpf.append(cpfvar)
        wheight.append(wheightvar)
        height.append(heightvar)
        age.append(agevar)
        card.append(cardvar)
        email.append(emailvar)
        cep.append(cepvar)
        not1.append(not1var)
        not2.append(not2var)
        not3.append(not3var)
        not4.append(not4var)
        avrg.append(avrgvar)
        year.append(yearvar)
        clas.append(clasvar)
        sex.append(sexvar)
        collor.append(collorvar)
        regist.append(registvar) #Todas as informações das variáveis de info. são adicionadas nas listas.
        if start==True: #Caso o usuário deseje continuar.
            opt2=input("Deseja continuar? S/N\n")
            opt2=opt2.capitalize()
            if opt2=="S":
                continue
            elif opt2=="N":
                break          
    while opt==2: #Checar aluno.
        tracer=int(input("Qual a matrícula do aluno?: "))
        tracer=tracer-1
        print("\nNome: {:}\nSobrenome: {:}\nRua e Número da Casa: {:}\nBairro: {:}\nCidade: {:}\nEstado: {:}\nPaís: {:}\nTelefone: {:}\nCPF: {:}\nPeso: {:}\nAltura: {:}\nIdade: {:}\nNúmero do Cartão: {:}\nEmail: {:}\nCEP: {:}\nNota do Primeiro Bimestre: {:}\nNota do Segundo Bimestre: {:}\nNota do Terceiro Bimestre: {:.2f}\nNota do Quarto Bimestre: {:}\nMédia: {:}\nSérie: {:}\nClasse: {:}\nSexo: {:}\nMatrícula: {:}".format(name[tracer],secondname[tracer],adress[tracer],slam[tracer],city[tracer],state[tracer],country[tracer],phone[tracer],cpf[tracer],wheight[tracer],height[tracer],age[tracer],card[tracer],email[tracer],cep[tracer],not1[tracer],not2[tracer],not3[tracer],not4[tracer],avrg[tracer],year[tracer],clas[tracer],sex[tracer],collor[tracer],regist[tracer]))
        if start==True: #Caso o usuário deseje continuar.
            opt2=input("Deseja continuar? S/N\n")
            opt2=opt2.capitalize()
            if opt2=="S":
                continue
            elif opt2=="N":
                break
    while opt==3: #Deletar registro.
        delete=int(input("Digite a matrícula a ser excluida: "))
        delete=delete-1
        del name[delete]
        del secondname[delete]
        del adress[delete]
        del slam[delete]
        del city[delete]
        del state[delete]
        del country[delete]
        del phone[delete]
        del cpf[delete]
        del wheight[delete]
        del height[delete]
        del age[delete]
        del card[delete]
        del email[delete]
        del cep[delete]
        del not1[delete]
        del not2[delete]
        del not3[delete]
        del not4[delete]
        del avrg[delete]
        del year[delete]
        del clas[delete]
        del sex[delete]
        del collor[delete]
        del regist[delete] #Funções que deletam as informações.
        if start==True: #Caso o usuário deseje continuar.
            opt2=input("Deseja continuar? S/N\n")
            opt2=opt2.capitalize()
            if opt2=="S":
                continue
            elif opt2=="N":
                break
    if opt==4: #Sair.
        break
    else: #Opção inexistente.
        print("Opção desconhecida. ERRO.")
        continue