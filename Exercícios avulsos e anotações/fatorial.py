def fatorial(n):


    if n == 1:
        return 1
    

    else:
        return n * fatorial(n - 1) #Recursividade, usando uma função dentro dela mesma
    

x = int(input("Digita ai: "))


a = fatorial(x)


print(a)


#Recursividade e fatorial
