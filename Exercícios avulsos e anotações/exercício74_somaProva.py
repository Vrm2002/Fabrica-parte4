import os
while True:
    try:
        a=float(input("Digite um número: "))
        b=float(input("Digite outro número: "))
        c=a+b
    except ValueError:
        os.system("cls")
        print("ERRO! Você digitou algum algarismo errado!")
        os.system("pause")
        os.system("cls")
    except:
        os.system("cls")
        print("ERRO DESCONHECIDO!")
        os.system("pause")
        os.system("cls")
    else:
        print("O resultado é: {:.2f}".format(c))
        opt=input("Deseja continuar? S\\N\n")
        opt=opt.capitalize()
        if opt=="S":
            os.system("cls")
            print("Obrigado por utilizar o programa.")
            os.system("pause")
            os.system("cls")
            break
        elif opt=="N":
            os.system("cls")
            os.system("pause")
            os.system("cls")
            continue
        else:
            os.system("cls")
            print("Opção desconhecida. Continuando...")
            os.system("pause")
            os.system("cls")
            continue
        #sistema simples de soma no entando em 37 linhas.