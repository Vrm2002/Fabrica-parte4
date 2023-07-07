import os

def somaImposto(x,y):
    custo=x
    imposto=y/100
    finalcost=custo+(custo*imposto)
    return finalcost

while True:
    try:
        a=float(input("Digite o custo do produto: "))
        b=float(input("Digite a porcentagem de Imposto: "))
    except ValueError:
        os.system("cls")
        print("Digite somente números.")
        os.system("pause")
        os.system("cls")
    else:
        os.system("cls")
        break
value=somaImposto(a,b)
print("O custo final será: {:.2f}R$.".format(value))
#Imprime um produto com uma taxa de imposto informada.