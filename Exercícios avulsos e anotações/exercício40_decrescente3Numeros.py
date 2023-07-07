a=float(input("Digite o primeiro número: "))
b=float(input("Digite o segundo número: "))
c=float(input("Digite o terceiro número: ")) #Lê os números.

if a==b and b==c and c==a: #Caso sejam iguais.
    print("Todos os números são iguais.")
elif a==b or b==c or c==a: #Caso apenas 2 sejam iguais.
    print("Erro. Existem dois números iguais.")
else: #Caso todos sejam diferentes.
    list=[a,b,c]
    list.sort(reverse=True)
    print("A ordem decrescente dos números é: {}".format(list))