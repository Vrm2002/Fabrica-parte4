a=float(input("Digite a primeira nota: ")) 
b=float(input("Digite a segunda nota: ")) #Lê as notas.
result=(a+b)/2
print("O resultado foi: %.2f"%(result)) #Imprime o resultado.

if result>=7: #Se o resultado foi maior ou igual a 7.
    print("Aprovado.")
elif (result>=5)and(result<=6.99): #Se o resultado for de 5 até 6,99.
    print("Em recuperação.")
else: #Qualquer nota fora das condições acima.
    print("Reprovado.")