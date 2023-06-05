import os
while True:
    try:
        a=int(input("Digite um número: "))
        b=int(input("Digite outro número: "))
        c=a/b
    except ValueError:
        print("Digite somente números.")
        os.system("pause")
        os.system("cls")
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")
        os.system("pause")
        os.system("cls")
    else:
        os.system("cls")
        print(c)
        os.system("pause")
        os.system("cls")