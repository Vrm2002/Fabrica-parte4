class Vendedor(): #Cria a classe


    def __init__(self,nome,vendas): #def __init__ é uma função que corresponde à própria classe, estão ligadas.
        self.nome = nome
        self.vendas = vendas


    def Vendeu(self,vendas): #Conseguimos criar mais funções dentro das classes. Sendo que seus parâmetros podem ser utilizados entre si.
        self.venda = vendas
        print(self.vendas)


    def Bateu_Meta(self,meta):
        if self.vendas > meta:
            print("Bateu a meta.")
        else:
            print("Não bateu a meta.")