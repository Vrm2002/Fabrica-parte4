print("Panificadora Pão de Ontem - Tabela de Preços")
value=float(input("Digite o preço do pão: ")) #Lê o valor do pão
soma=value
for i in range(1,51): #Numera e soma o valor do pão por quantidade.
    print("{:d}- R$ {:.2f}".format(i,soma))
    soma=soma+value