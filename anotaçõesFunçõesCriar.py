def hello(nome):
    print("Olá ",nome)
hello("Ederson")
#def cria uma função. Esta acima imprimirá "olá Ederson".

def hello(name,age):
    print("Olá",name,"\nSua idade é:",age)
hello("Ederson",25)
#É posível utilizar mais de um parâmetro.

def calc_pag(qtd_horas,valor_hora):
    hrs=float(qtd_horas)
    taxa=float(valor_hora)
    if hrs<=40:
        sal=hrs*taxa
    else:
        h_excd=hrs-40
        sal=40*taxa+(h_excd*(1.5*taxa))
    print(sal)
calc_pag(40,60)
#calcula o valor do salario.

def soma(x,y):
    result=x+y
    return result 
#Return serve para colocar uma saida para a função. Para no caso de querer manipular o retorno dessa função.

def invert(nome,sobrenome):
    nomeInverse=sobrenome+", "+nome
    return nomeInverse
nome=input("Nome: ")
sobrenome=input("Sobrenome: ")
inverse=invert(nome,sobrenome)
print("Olá", inverse)
#função que inverte nome e sobrenome de lugares.

def parimpar(num):
    result=num%2
    if result==0:
        return True
    else:
        return False 
while True:
    num=int(input("Digite um número: "))
    if parimpar(num):
        print("É par")
    else:
        print("É impar")
#O código acima confirma se um número é par ou não usando funções.