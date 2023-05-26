numbers=[]
test=[False]
while True:
    num=input("Digite um número: ") 
    if num=="x" and test[0]==False:
        print("Não foi digitado número algum. Tente novamente.")
        continue
    if num=="x" and test[0]==True:
        print("O maior número é:",max(numbers),"\nO menor número é:",min(numbers),"\nA soma de todos é:",sum(numbers))
        break
    num=int(num)
    test[0]=True
    numbers.append(num)