sal=float(input("Digite o salário do funcionário: ")) #Lê o salário.

if (sal<500): #Caso o salários seja menor do que 500.
    reaj=(sal*0.15)+sal
    print("Salário inicial: {:.2f} \nSalário reajustado: {:.2f} \nTaxa de Reajuste: 15%".format (sal,reaj))
elif (sal>=500) and (sal<=1000): #Seja de 500 até 1000.
    reaj=(sal*0.10)+sal
    print("Salário inicial {:.2f} \nSalário reajustado: {:.2f} \nTaxa de Reajuste: 10%".format (sal,reaj))
elif (sal>1000): #Mais que 1000.
    reaj=(sal*0.05)+sal
    print("Salário incial {:.2f} \nSalário reajustado: {:.2f} \nTaxa de Reajuste: 5%".format (sal,reaj))
elif (sal==0): #Caso o salário seja 0.
    print("Salário inexistente.")