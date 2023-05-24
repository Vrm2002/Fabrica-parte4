num=int(input("Digite um número: ")) #Lê o número.
while num>0: #Enquanto for maior que zero.
    test1=num%2
    test2=num%3
    test3=num%5
    test4=num%7
    test5=num%11 #Teste dos números primos do 2 ao 11.

    if num==11: 
        print("11","\n7","\n5","\n3","\n2")
        break
    elif num==10 or num==9 or num==8 or num==7:
        print("7","\n5","\n3","\n2")
        break
    elif num==5:
        print("5","\n3","\n2")
        break
    elif num==3:
        print("\n3","\n2")
        break
    elif num==2: #Caso os números digitados sejam do 2 ao 11. Ele já imprime os primos que estão nas variáveis de testes.
        print(2)
        break
    elif test1==0 or test2==0 or test3==0 or test4==0 or test5==0: #Testa números acima de 11. Caso o resto dos testes seja 0, o número não é imprimido.
        num=num-1
        continue
    elif test1!=0 and test2!=0 and test3!=0 and test4!=0 and test5!=0: #Testa números acima de 11. Caso o resto dos testes seja 0, o número é imprimido.
        print(num)
        num=num-1
        continue