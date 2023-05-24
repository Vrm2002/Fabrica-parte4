name=input("Nome do primeiro produto: ")
value=float(input("O valor do primeiro produto: ")) #Lê o nome e o valor do produto.

name2=input("Nome do segundo produto: ")
value2=float(input("O valor do segundo produto: ")) #Lê o nome e o valor do produto.

name3=input("Nome do terceiro produto: ")
value3=float(input("O valor do terceiro produto: ")) #Lê o nome e o valor do produto.

name=name.capitalize()
name2=name2.capitalize()
name3=name3.capitalize() #Garante que essas variáveis terão a primeira letra maiúscula.
valist=[value,value2,value3] #Lista as 3 variáveis de valores.
bestval=min(valist) #Escolhe a com menos valor entre elas.

if bestval==value: #O código abaixo printa o nome do produto e o seu valor CASO ele tenha o menor valor possível.
    print("{:s} é o produto mais barato para se comprar. Seu valor é: {:.2f}".format(name,value))
elif bestval==value2:
    print("{:s} é o produto mais barato para se comprar. Seu valor é: {:.2f}".format(name2,value2))
elif bestval==value3:
    print("{:s} é o produto mais barato para se comprar. Seu valor é: {:.2f}".format(name3,value3))
else: #Qualquer outra situação fora as acima.
    print("Erro. Existem números iguais.")