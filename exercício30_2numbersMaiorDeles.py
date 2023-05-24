a=float(input("Digite o primeiro número: "))
b=float(input("Digite o segundo número: ")) #Lê os números.

if a>b: #Se a for maior que b.
    print("O maior número é: %.0f"%(a))
elif a<b: #Se b for maior que a.
    print("O maior número é: %.0f"%(b))
elif a==b: #Se forem iguais.
    print("Ambos os números são iguais.")