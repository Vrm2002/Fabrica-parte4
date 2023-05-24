a=[1.29,24,"Olá",True] #Uma lista é formada de uma variável com várias informações dentro, no eixo X.
print(type(a)) #Imprime o tipo da variável. Que é "list".

b=[1.30,25,"Hello",False,[1,2]] #sublistas conseguem ser criadas dentro de listas.
print(len(b)) #função len irá informar somente 5 itens, e não 6. Visto que a sublista conta somente como um objeto.

c=[3,67,"gato",[36,37]]
print(c[2][0]) #Este código imprimirá a letra "g", da variável "gato". O primeiro número decide a variável de índice 2, e então, dentro desta variável, o índice 0.
# O exemplo acima funciona com sublistas.
print(c[3][2]) #Imprimirá o "37".
print("37" in c) #O in não identificará o 37 por estar em uma sublista.
print([1,2]+[3,4]) #imprimirá ambas as listas na ordem 1,2,3,4. Não somará os números. A concatenação funciona com listas. Assim como a multiplicação.
print(min(c)) #Pega o menor elemento da lista.
print(max(c)) #Pega o maior elemento da lista.
print(sum(c)) #Soma os elementos da lista. (funções)

frutas=["banana","maçã","cereja"] #declarar as informações da lista.
frutas[0]="Pêra" #Colocando o índice na frente da variável, conseguimos trocar esse valor em específico dentro da própria variável.
frutas[-1]="Laranja" #Mesma coisa do de cima.

list1=["a","b","c","d","e","f"]
list1[1:3] = ["x","y"] #Irá trocar o b pelo x, e o c pelo y. 
print(list1) #Imprime a lista atualizada.

list2=["a","b","c"]
list2[1:3] = [] #Isso trocará "b" e "c" por uma lista vazia, removendo ambos.

list3=["a","d","f"]
list3[1:1]=["b","c"]
list3[4:4]=["e"]
print(list3) #O código acima adiciona b,c,e na lista. Colocando ambos valores absolutos iguais nos índices.

list4=["um","dois","tres"]
del list4[1] #O delete serve para deletar algum índice de uma forma melhor que o slice.
print(list4) #Deleta o índice 1, que é a palavra "dois".

list5=["a","b","c","d","e","f"]
del list5[1:5]
print(list5) #Deleta do índice 1 ao 4, 5 sendo limite. Deletará: "b","c","d","e".

list6=[81,82,83]
list6.append(84) #O var.append(content) faz essa adição.
print(list6) #O código adiciona um elemento adicional no final da lista.

list7=[88,81,82,83]
list7.sort() #Altera para ordem crescente. Se for string será alfabética.
print(list7) #Printa o código acima.
list7.sort(reverse=True) #Trocará a ordem para decrescente. String será a ordem alfabética contrária.

list8=[1,2,3,4,5,6,7,8,9]
print(list8.index(4)) #Informa o índice que está o número "4", que é o índice 3.

list9=[88,81,82,84]
list9.insert(1,100) #O primeiro número é o índice onde seu número deve estar. O segundo é o número informado.
print(list9) #Informará [88,100,81,82,83]. Ele não retira o número 81, ele fica no lugar dele e este por si move para o índice da frente.

list10=[88,81,88,82,88,83]
print(list10.count(88)) #A função count também funciona com listas.

list11=[1,2,3,4]
list11.pop() #Remove o último da lista.
list11.pop(0) #Remove o índice informado.
print(list11)