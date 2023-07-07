par=[]
impar=[]
for i in range(10): #Lê os números.
    num=int(input("Digite um número: "))
    if num%2==0:
        par.append(num)
    elif num%2!=0:
        impar.append(num)
    elif num<0:
        print("Número negativo não entra para as categorias.")
    else:
        print("O que você digitou não foi um número.")
print("\nOs pares que você digitou são: ") 
for i in par: #Imprime os pares.
    print(i)
print("\nE os ímpares são: ")
for i in impar: #Imprime os impares.
    print(i)