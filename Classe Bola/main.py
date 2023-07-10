from Bola import *
from os import system as ss

ball = Bola(10,"Ferro","Preto") #Informações prè determinadas.

while True:
    opt = input("BOLA -----------------------------------\n1. Trocar a cor da Bola\n2. Mostrar a cor da bola\n0. Sair\n\nEscolha: ") #Menu


    if opt == "1": #Trocar cor
        ss("cls")
        collor = input("Digite a nova cor: ")
        ss("cls")
        print("Cor alterada!")
        ball.collor_change(collor)
        ss("pause")
        ss("cls")
    

    elif opt == "2": #Mostrar cor
        ss("cls")
        print("Cor atual ----------------------------")
        ball.collor_show()
        ss("pause")
        ss("cls")
    

    elif opt == "0": #Sair
        ss("cls")
        print("Obrigado por utilizar o programa.")
        break
    

    else:#Nenhuma opção.
        ss("cls")
        print("Opção Inexistente.")
        ss("pause")
        ss("cls")

