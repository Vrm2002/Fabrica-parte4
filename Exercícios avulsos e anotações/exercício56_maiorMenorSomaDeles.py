numbers=[]
while True:
    num=input("Digite um número: ") #Lê um número.
    if num=="x": #Caso o usuário digite "x", o código para.
        print("O maior número é:",max(numbers),"\nO menor número é:",min(numbers),"\nA soma de todos é:",sum(numbers)) #Printa os resultados.
        break
    num=int(num) #Transforma a string em inteiro.
    numbers.append(num) #Adiciona o inteiro digitado na lista.