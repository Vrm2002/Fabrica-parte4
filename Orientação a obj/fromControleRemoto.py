from ControleRemoto import *
from os import system as st

while True:     
    button = input("Insira um botão: ")

    control = ControleRemoto("Black",button,1.34,3.34,2.24)

    '''print(control.collor)
    print(control.buttons)
    print(control.height)
    print(control.lenght)
    print(control.thick)'''

    onoff=control.turn_on_off()

   

    #print(onoff)


    if onoff == True:
        #st("cls")
        print("TV Ligada.")
        #st("pause")
        #st("cls")
   

    else:
        #st("cls")
        print("TV Desligada.")
        #st("pause")
        #st("cls")'''