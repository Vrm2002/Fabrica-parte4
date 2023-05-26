num=[]
for b in range(5): #Repete 5 vezes dentro da variavel b.
    a=int(input("Digite um número para ser adicionado na conta: ")) #Lê os numeros.
    num.append(a) #Adiciona eles numa lista.
result=sum(num)/5 #Média.
print("A soma dos números é:",sum(num),"\nE sua média é:",result) #Imprime a soma e a média.