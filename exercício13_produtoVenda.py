prod=input("Digite o nome do produto: ") #Lê o nome do produto.
quant=int(input("Digite a quantidade comprada do produto: ")) #Lê a quantidade do produto.
value=float(input("Digite o valor do produto: ")) #Lê o valor do produto.
per=float(input("De 1 a 100, digite o percentual de desconto: ")) #Lê a porcentagem do desconto.

totalprod=(value-(value*(per/100))) #Realiza o desconto DO PRODUTO INDIVIDUALMENTE.
totalfinal=(totalprod*quant) #Une o valor do produto com a quantidade, dando no valor total.

print("O produto %s, na quantidade %d, vale %.2f"%(prod,quant,totalfinal)) #Imprime as informações em ordem.