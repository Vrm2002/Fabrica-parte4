temp=[]
month=[]
year=[]
validate=False #Variável de teste.
while True:
    tempv=input("Digite a temperatura em Celsius: ") #Lê a temperatura
    testemp=tempv.isdigit()
    if testemp==True: #Caso a temperatura lida seja um digito.
        validate=True
        tempv=float(tempv)
        temp.append(tempv)
    elif testemp==False: #Caso não seja um digito.
        if validate==False: #Caso ele não tenha digitado nenhuma informação anteriormente, antes de desligar o programa.
            if tempv=="X" or tempv=="x":
                print("Você não adicionou nenhuma informação.")
                break
            else: #Caso ele digite algo que não foi o X.
                print("Erro. Você não digitou o algarismo certo.")
                continue
        elif validate==True: #Caso tenha informação nas listas.
            if tempv=="X" or tempv=="x": #Caso ele digite o X para fechar o código.
                break
            else: #Caso ele não digite o X.
                print("Erro. Você não digitou o algarismo certo.")
                continue 
    
    monthv=input("Mês em que ela ocorreu: ") #Lê o mês.
    testmonth=monthv.isdigit()
    if testmonth==True: #Se for digito.
        monthv=int(monthv)
        if monthv>0 and monthv<13: #Se for somente entre o mes 1 ao 12.
            month.append(monthv)
        else: #Caso não esteja entre os 12 meses.
            validate=False
            print("Erro!")
            break
    elif testmonth==False: #Caso não seja digito.
        validate=False
        print("Erro!")
        break
    
    yearv=input("Ano em que ela ocorreu: ") #Lê o ano.
    testyear=yearv.isdigit()
    if testyear==True: #Se for digito.
        yearv=int(yearv)
        year.append(yearv)
    elif testyear==False: #Se não for.
        validate=False
        print("ERRO!")
        break

if validate==True: #Caso nenhum erro tenha acontecido durante os digitos. A variável de controle permanecerá verdadeira e prosseguirá para os resultados.
    cont=0
    for i in temp:
        cont+=1
    medtemp=sum(temp)/cont

    less=min(temp)
    more=max(temp)
    indexmin=temp.index(less)
    indexmax=temp.index(more)
    lessmonth=month[indexmin]
    moremonth=month[indexmax]
    lessyear=year[indexmin]
    moreyear=year[indexmax]

    print("\nA maior temperatura informada foi de {:.2f} graus celsius em {:d}/{:d}.\nA menor informada foi {:.2f} graus celsius em {:d}/{:d}.\nA média de todas as temperaturas foi {:.2f} graus celsius.".format(more,moremonth,moreyear,less,lessmonth,lessyear,medtemp))
elif validate==False: #Caso algum erro aconteça.
    print("Ocorreu algum erro durante a coleta de informações ou então o programa foi encerrado sem coletar informação alguma. Por favor tente novamente.")