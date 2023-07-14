class Bola():


    def __init__(self,circun,material,cor): 
        self.circun = circun
        self.material = material
        self.cor = cor


    def collor_change(self,newcollor): #Trocar cor
        self.cor = newcollor
    

    def collor_show(self): #Mostrar cor
        print(self.cor)
