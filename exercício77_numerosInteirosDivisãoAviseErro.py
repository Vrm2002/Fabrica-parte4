import os
try:
    a=int(input("Digite um número: "))
    b=int(input("Digite outro número: "))
    c=a/b
except ZeroDivisionError:
    os.system("cls")
    print("Não é possível dividir por 0.")
    os.system("pause")
    os.system("cls")
except ValueError:
    os.system("cls")
    print("Digite somente números inteiro!")
    os.system("pause")
    os.system("cls")
except:
    os.system("cls")
    print("Erro desconhecido!")
    os.system("pause")
    os.system("cls")
else:
    os.system("cls")
    print("O resultado é: {:d}".format(c))
    os.system("pause")
    os.system("cls")
#código que divide e avisa o usuário caso dê algum erro.