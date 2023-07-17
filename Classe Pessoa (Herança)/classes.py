class Person(): #Super classe pessoa


    def __init__(self,name,age:int,adress,city,state):
        self.name = name
        self.age = age
        self.adress = adress
        self.city = city
        self.state = state


    def relatorio(self):
        print("Nome: {:s}\nIdade: {:d}\nEndereço: {:s}\nCidade: {:s}\nEstado: {:s}\n".format(self.name,self.age,self.adress,self.city,self.state))
    

class Student(Person): #Subclasse aluno
    

    def __init__(self,mensal:float,name,age:int,adress,city,state):
        super().__init__(name,age,adress,city,state) #herança
        self.mensal = mensal
        print("=================================\nSeja Bem Vindo Aluno!\n")
        super().relatorio() #herança
        print("Mensalidade: {:.2f}\n=================================".format(self.mensal))


class Professor(Person): #subclasse professor


    def __init__(self,salary:float,name,age:int,adress,city,state):
        super().__init__(name,age,adress,city,state) #herança
        self.salary = salary
        print("=================================\nSeja Bem Vindo Professor!\n")
        super().relatorio() #herança
        print("Salário: {:.2f}\n=================================".format(self.salary))