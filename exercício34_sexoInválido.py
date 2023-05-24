a=input("Digite seu sexo: F(Feminino)/ M(Masculino) / O(Outros): ") #Lê o sexo.
a=a.capitalize() #Garante que a letra digitada foi maiúscula.

if a=="F": #Caso seja feminino.
    print("Você é do sexo feminino.")
elif a=="M": #Caso seja Masculino.
    print("Você é do sexo masculino.")
elif a=="O": #Caso seja outro.
    print("Você não é do sexo masculino nem feminino.")
else: #Caso não seja nenhum deles.
    print("Sexo Inválido.")