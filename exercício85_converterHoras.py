import os

def hourvert(x,y):
    hours=x-12
    minuts=y

    if x<12 and x>=0:
        hours=x
        finalhour=hours,":",minuts," AM"
        return finalhour
    elif x==12:
        hours=x
        finalhour=hours,":",minuts," PM"
        return finalhour
    else:
        finalhour=hours,":",minuts," PM"
        return finalhour

while True:
    try:
        a=int(input("Digite as Horas: "))
        b=int(input("Digite os minutos: "))
    except:
        os.system("cls")
        print("Digite somente números inteiros nas horas e nos minutos.")
        os.system("pause")
        os.system("cls")
    else:
        os.system("cls")
        break

hourcon=hourvert(a,b)
if hourcon[0]<0:
    print("Erro na hora informada.")
else:
    print("Hora informada: {:.0f}{:s}{:d}{:s}".format(hourcon[0],hourcon[1],hourcon[2],hourcon[3]))
#Converte as horas pro do formato de 24 pra 12.