import os

def negpos(x):
    if x>0:
        return "P"
    elif x==0:
        return "0"
    elif x<0:
        return "N"
    else:
        return "Not a number."

while True:
    try:
        a=int(input("Digite um número:  "))
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

val=negpos(a)
print(val)
#Retorna se um número é negativo, positivo ou neutro.