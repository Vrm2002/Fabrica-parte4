class Square():
    

    def __init__(self): #Tamanho do lado do quadrado somente.
        self.sidelen = 0
    

    def show_area(self): #Calcula a área do quadrado.
        self.area = self.sidelen**2
        print(self.area)
        print(self.sidelen)
    

    def change_side(self,newside): #Troca o lado.
        self.sidelen = newside