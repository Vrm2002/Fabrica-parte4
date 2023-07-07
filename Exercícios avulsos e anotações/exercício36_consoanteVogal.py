a=["A","E","I","O","U","Y"] #LISTA de Vogais.
b=["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Z"] #LISTA de Consoantes.

letter=input("Digite uma letra: ") #Lê a letra.
letter=letter.capitalize() #Garante que a letra digitada seja maiúscula.
test=letter.isdigit() #Informa se o que foi digitado foi número ou letra.

if test==False: #Testa o que foi digitado. Se for número não será considerado.
    if letter in a: #Se for vogal.
        print("A letra digitada é uma vogal.")
    elif letter in b: #Se for Consoante.
        print("A letra digitada é uma consoante.")
else: #Se não for nenhum.
    print("O que você digitou não foi uma letra.")