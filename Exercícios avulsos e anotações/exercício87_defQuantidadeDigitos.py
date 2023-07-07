import os

def contadorNum(x):
    cont=0
    var=str(x)
    for i in var:
        cont+=1

while True:
    try:
        a=int(input("Digite um número: "))

contador=contadorNum(a)
print("Quantidade de digitos: {:d}".format(contador))
#Conta a quantidade de caracteres.