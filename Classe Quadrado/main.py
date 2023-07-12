from os import system as ss
from Quadrado import *

lock = False #Não permite que o usuário continue o código sem informar um valor antes.

while True: 
    opt = input("QUADRADO------------------------------------------------\n1. INFORMAR TAMANHO DO LADO DO QUADRADO\n2. CALCULAR ÁREA\n0. SAIR\n\nESCOLHA: ")
    #menu


    if opt == "1": #Informar lado do quadrado
        try:
            ss("cls")
            newside = float(input("INFORME O TAMANHO DO LADO: "))
        
        except ValueError:
            ss("cls")
            print("DIGITE SOMENTE NÚMEROS.")
            ss("pause")
            ss("cls")
        
        else:
            ss("cls")
            square = Square()
            square.change_side(newside)
            lock = True
            print("VALOR ALTERADO COM SUCESSO!")
            ss("pause")
            ss("cls")
    

    elif opt == "2": #Calcular area
        ss("cls")

        if lock == True:
            print("ÁREA DO QUADRADO E TAMANHO DO LADO------------------------------------\n")
            square.show_area()
            ss("pause")
            ss("cls")
        

        else:
            ss("cls")
            print("VOCÊ DEVE INFORMAR O VALOR DO LADO DO QUADRADO PRIMEIRO.")
            ss("pause")
            ss("cls")
    
    elif opt == "0": #Sair
        ss("cls")
        print("OBRIGADO POR UTILIZAR O PROGRAMA.")
        break


    else: #No caso de ser uma opção inexistente
        ss("cls")
        print("OPÇÃO INEXISTENTE.")
        ss("pause")
        ss("cls")
