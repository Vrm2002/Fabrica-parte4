while True:
    print(" -------------------------------------\n","             CALCULADORA          \n","-------------------------------------")
    option=input("BEM VINDO! O QUE VOCÊ DESEJA CALCULAR?\n1 - ADIÇÃO\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n5 - EXPONENCIAÇÃO\n6 - RAIZ QUADRADA\n7 - ÁREA DE UM QUADRADO\n8 - VOLUME DE UM CUBO\n9 - MÉDIA DE 4 NÚMEROS.\n10 - FATORIAL\n0 - SAIR\n----------------------\n")
#A variável option define as opções.
    if option=="1": #Caso digite 1 pra variável option. Cairá aqui na adição.
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o segundo número: "))
        result=a+b
        print("O resultado foi {:.2f}".format(result))
        continue
    elif option=="2": #Caso digite 2 pra variável option. Cairá aqui na subtração.
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o segundo número: "))
        result=a-b
        print("O resultado foi {:.2f}".format(result))       
        continue
    elif option=="3": #Caso digite 3 pra variável option. Cairá aqui na multiplicação..
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o segundo número: "))
        result=a*b
        print("O resultado foi {:.2f}".format(result))       
        continue
    elif option=="4": #Caso digite 4 pra variável option. Cairá aqui na divisão.
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o número que divide o primeiro: "))
        result=a/b
        print("O resultado foi {:.2f}".format(result))      
        continue 
    elif option=="5": #Caso digite 5 pra variável option. Cairá aqui na exponenciação.
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o número que será o exponencial: "))
        result=a**b
        print("O resultado foi {:.2f}".format(result))      
        continue
    elif option=="6": #Caso digite 6 pra variável option. Cairá aqui na raiz quadrada.
        a=float(input("Digite um número para descobrir a raiz quadrada."))
        result=a**0.5
        print("A raiz quadrada do número digitado é {:.2f}".format(result))      
        continue
    elif option=="7": #Caso digite 7 pra variável option. Cairá aqui na área de um quadrado.
        a=float(input("Digite o tamanho em centímetros de um dos lados do quadrado: "))
        result=a**2
        print("A área deste quadrado é {:.2f}".format(result))        
        continue 
    elif option=="8": #Caso digite 8 pra variável option. Cairá aqui no volume de um cubo..
        a=float(input("Digite o comprimento de uma das arestas do cubo: "))
        result=a**3
        print("O volume do cubo é {:.2f}".format(result))      
        continue 
    elif option=="9": #Caso digite 9 pra variável option. Cairá aqui na média.
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o segundo número: "))
        c=float(input("Digite o terceiro número: "))
        d=float(input("Digite o quarto número: "))
        result=(a+b+c+d)/4
        print("A média dos quatro números digitados é {:.2f}".format(result))     
        continue 
    elif option=="10": #Caso digite 10 pra variável option. Cairá aqui no fatorial.
        a=int(input("Digite um número para ter seu fatorial: "))
        fat=1
        b=2
        while b<=a:
            fat=fat*b
            b=b+1
        print("O resultado é {:d}".format(fat))     
        continue
    elif option=="0": #Caso digite 0 pra variável option. Cairá pra parar o código.
        break
    else: #Caso digite qualquer outra coisa pra variável option. Cairá aqui na mensagem de erro.
        print("Erro. Opção não encontrada.")    
        continue