import os

def soma(a,b,c):
    result=a+b+c
    return result

while True:
    try:
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o segundo número: "))
        c=float(input("Digite o terceiro número: "))
    except ValueError:
        os.system("cls")
        print("Digite somente números.")
        os.system("pause")
        os.system("cls")
    except:
        os.system("cls")
        print("Erro desconhecido.")
        os.system("pause")
        os.system("cls")
    else:
        break
val1=soma(a,b,c)
print("O valor é: {:.0f}".format(val1))
#Lê 3 números e imprime a soma deles.