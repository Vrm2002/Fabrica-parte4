a="ederson" #Variável declarada
print(len(a)) #A função conta o número de algarismos em uma variável string.
print(a.capitalize()) #Deixa o primeiro algarismo em letra maiúscula.
print(a.casefold()) #O primeiro algarismo se torna em letra minúscula.
print(a.upper()) #Deixa todos os algarismos maiúsculos.
print(a.lower()) #Deixa todos os algarismos minúsculos.
print(a.islower()) #Pergunta se a variável é em letra minúscula. True or False.
print(a.isupper()) #Pergunta se a variável é em letra maiúscula. True or False.

b="12345"
c="12345abc"
print(b.isdigit()) #A função var.isdigit() diz se uma variável possui somente números. Esta é [True].
print(c.isdigit()) #Esta é [False].

d="Ederson Roberto"
print(d.replace("Roberto","Costa")) #A função var.replace(content) substitui temporariamente as informações de uma string.

e="Ederson-Roberto-Costa"
print(e.split("-")) #Irá substituir o sinal indicado por vírgulas. 

f="Ederson Roberto Costa"
print(f.find("Costa")) #Acha o primeiro índice do string indicado. Da esquerda para a direita.
print(f.rfind("Costa")) #Acha o primeiro índice do string indicado. Da direita para a esquerda. 
print("Costa" in f) #Vai perguntar ao código se existe o conteúdo mencionado na variável f
print(f.count("a")) #Conta quantas vezes um caractér foi encontrado numa variável.

g="Olá, mundo!"
print(g[0]) #Escolhe uma posição especifica de uma string para imprimir. Este imprimirá a letra "O"
print(g[1]) #Este imprimirá o "l".
print(g[-1]) #Pode-se usar a ordem negativa também. Este imprimirá o "!".
print(g[0:3]) #Adicione ":" e mais um índice e tudo será imprimido até ele, sem contar o índice final.
print(g[5:]) #Imprime todo o conteúdo a partir do índice informado.
print(g[:3]) #Imprime todo o conteúdo até o índice informado, sem contar ele.