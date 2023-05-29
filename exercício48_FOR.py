nome=["Pedro","João","Leticia"]
for n in nome: #Função For-variável=Função in-Lista +print fará com que os nomes sejam printados um por vez. Visto que uma informação por vez é passada da lista para a variável.
    print(n)
for n in nome[1]: #Caso seja somente algum índice de uma lista ou uma variável string em seu lugar, cada letra será imprimida em uma linha.
    print(n)
for n in nome: #A função break pode ser utilizada também.
    print(n)
    if n=="João":
        break
for n in nome: #Continue também pode ser usado. Ele não imprimirá João, ele voltará para o código e imprimirá pedro e leticia.
    if n=="João":
        continue
    print(n)

for x in range(6): #A função range. Ela começa em 0 por padrão e irá imprimir números até o limito informado nos parâmetros. Neste caso ele imprimirá somente do 0 ao 5, seis números.
    print(x)
for x in range(2,6): #Imprimirá do 2 até o 5. Sempre terminará em 1 a menos.
    print(x)
for x in range(2,10,2): #imprimirá do 2 ao 8, de 2 em 2. O terceiro número define uma sequencia.
    print(x)
for x in range(100,0,-1): #Imprimirá do 100 ao 1. Caso o número de sequencia seja negativo, ele contará para trás.
    print(x)

for i in range(5): #O I só terá seu valor aumentado quando J completar um loop até o numero 5, quando ele chega no 5, o i aumenta para 1. Um loop é gerado até que ambos chegem no valor máximo, que no caso de i é 4 e o de j é 5.
    for j in range(6):
        print(i,j)

list=[]
for i in range(5): #Inputs podem ser usados para ser utilizados junto da função append para preencherem listas no FOR.
    list.append(input("Digite um ítem: "))
for i in list: #Coloque uma variável in lista e mande printar a lista para receber cada ítem da lista.
    print(i)