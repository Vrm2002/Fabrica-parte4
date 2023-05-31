eleinum=int(input("Digite a quantidade de candidatos: ")) #Lê o número de candidatos
renato=0
michel=0
wesley=0
nul=0

for i in range(eleinum): #Hora da votação
    voto=input("Qual o seu voto?\n1- Renato Russo\n2- Michel Teló\n3- Wesley Safadão\n")
    test=voto.isdigit() #Teste pra ver se o voto é um digito.
    if test==True:
        voto=int(voto)
        if voto==1: #Deputado 1
            renato=renato+1
        elif voto==2: #Deputado 2
            michel=michel+1
        elif voto==3: #Deputado 3
            wesley=wesley+1
        else: #Nenhum dos deputados
            print("Voto nulo\n")
            nul=nul+1
    else:
        print("O que você digitou não foi um número.")
print("TOTAL DE VOTOS\n1- Renato Russo: {:d}\n2- Michel Teló: {:d}\n3- Wesley Safadão: {:d}\nVotos Nulos: {:d}".format(renato,michel,wesley,nul)) #Imprime os resultados