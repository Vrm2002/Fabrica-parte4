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