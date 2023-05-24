a=int(input("Digite um valor para ser reduzido: ")) #Lê o número.
cont=0 #defina o número base do contador.

while a>0: #Entra no laço caso o número informado seja maior que 0.
    a=a-1 #Diminui o número informado até 0.
    cont=cont+1 #Aumenta o número do contador.
if a==0: #Caso o número seja igual a 0.
    print("O número total de vezes que este número pode ser reduzido até 0 é de {:d} vezes.".format(cont)) #O contador é usado como o número de vezes em que o número foi reduzido.