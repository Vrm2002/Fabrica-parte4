minnot=0
maxnot=10
medmin=7 #Nota Mínima, Nota Máxima e Média Mínima respectivamente.
a=float(input("Digite a primeira nota: "))
b=float(input("Digite a segunda nota: ")) #Leem as notas.
med=(a+b)/2 #Faz a média.

if med>=medmin and med<=maxnot: #Se a média for maior ou igual a média mínima e menor ou igual a nota máxima.
    print("Aprovado")
    if med==maxnot: #Se for igual a nota máxima.
        print("com distinção.")
elif med<medmin and med>=minnot: #Se a média for menor do que a média mínima e maior ou igual a nota mínima.
    print("Reprovado.")
else:
    print("Média inválida.")