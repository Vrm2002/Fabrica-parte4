a=int(input("Digite um número, o início: ")) #Pede o começo.
b=int(input("Digite outro número, o final: ")) #Pede o fim.
soma=[]
for c in range(a+1,b): #Gera os números que estão entre a e b.
    print(c)
    soma.append(c) #Adiciona os números em uma lista.
print("Soma dos números que estão no meio:",sum(soma)) #Printa a soma dos elementos da lista.