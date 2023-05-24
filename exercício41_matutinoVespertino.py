a=input("Em qual turno você estuda? Matutino, Vespertino ou Noturno? (M/V/N)\n") #Lê a letra.
a=a.capitalize() #Garante que ela seja maiúscula.

if a=="M": #Se for matutino.
    print("Bom dia!")
elif a=="V": #Se for vespertino.
    print("Boa tarde!")
elif a=="N": #Se for noturno.
    print("Boa noite!")