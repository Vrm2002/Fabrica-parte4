from Retangulo import *
from os import system as ss


lock = False
rectan = Rectangle()


while True:
    opt = input("PROGRAMA DE CALCULO DE AREA -----------------------------------\n\n1. INFORMAR VALOR DOS LADOS DO LOCAL\n2. MOSTRAR OS LADOS DO LOCAL\n3. CALCULAR ÁREA E PERÍMETRO DO LOCAL\n0. SAIR\n\nESCOLHA: ")


    if opt == "1":


        try:
            ss("cls")
            width = float(input("INFORME O VALOR DA BASE: "))
            ss("cls")
            height = float(input("INFORME O VALOR DA LARGURA: "))
        

        except ValueError:
            ss("cls")
            print("DIGITE SOMENTE NÚMEROS!")
            ss("pause")
            ss("cls")
        

        else:


            if width < 0 or height < 0:
                ss("cls")
                print("NÚMEROS NEGATIVOS FORAM INFORMADOS NA COLETA DE DADOS. PORTANTO A AÇÃO NÃO PODE SER EFETUADA!")
                ss("pause")
                ss("cls")
            

            else:
                ss("cls")
                rectan.side_change(width,height)
                lock = True
                print("VALORES ALTERADOS COM SUCESSO!")
                ss("pause")
                ss("cls")
        

    elif opt == "2":


        if lock == True:
            ss("cls")
            print("VALOR DA BASE E DA LARGURA RESPECTIVAMENTE:")
            rectan.side_show()
            ss("pause")
            ss("cls")
        

        else:
            ss("cls")
            print("NÃO HÁ NENHUM VALOR INFORMADO.")
            ss("pause")
            ss("cls")
    

    elif opt == "3":


        if lock == True:
            ss("cls")
            print("VALOR DA ÁREA DO LOCAL E DO PERÍMETRO RESPECTIVAMENTE:")
            rectan.area_per_calc()
            ss("pause")
            ss("cls")
        

        else:
            ss("cls")
            print("NÃO HÁ VALORES INFORMADOS DE BASE E LARGURA.")
            ss("pause")
            ss("cls")
    

    elif opt == "0":
        ss("cls")
        print("OBRIGADO POR UTILIZAR O PROGRAMA!")
        break


    else:
        ss("cls")
        print("OPÇÃO INEXISTENTE!!!")
        ss("pause")
        ss("cls")