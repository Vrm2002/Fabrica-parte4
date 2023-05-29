list=[]
list2=[]
for i in range(6): #Lê os números.
    list.append(int(input("Digite um número: ")))
for i in list: #Multiplica por 5 cada elemento da lista e atribui eles pra lista2.
    i=i*5
    list2.append(i)
print(list,"\n",list2)