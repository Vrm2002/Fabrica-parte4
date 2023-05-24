a=float(input("Digite o primeiro número: "))
b=float(input("Digite o segundo número: "))
c=float(input("Digite o terceiro número: ")) #Lê os números.

if a==b and b==c and a==c: #Caso todos os números sejam iguais.
    print("Todos os números são iguais.")
elif a==b: #Se a e b forem iguais.
    print("Os números {:.2f} e {:.2f} são iguais.".format(a,b))
elif b==c: #Se b e c forem iguais.
    print("Os números {:.2f} e {:.2f} são iguais.".format(b,c))
elif c==a: #Se c e a forem iguais.
    print("Os números {:.2f} e {:.2f} são iguais.".format(c,a))
else: #Caso sejam diferentes.
    list=[a,b,c] #Lista com os números mensionados.
    print("O maior número foi: ",max(list)) #Imprime o maior número da lista.