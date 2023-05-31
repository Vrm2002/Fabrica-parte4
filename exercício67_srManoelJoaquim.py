print("Lojas Quase Dois - Tabela de Preços") #Título
value=1.99
for i in range(1,51): #Imprime a tabela de compra.
    print("{:d}- R$ {:.2f}".format(i,value))
    value=value+1.99