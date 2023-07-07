class ControleRemoto():


    def __init__(self,collor,buttons,lenght,height,thick):
        self.collor = collor
        self.buttons = buttons
        self.lenght = float(lenght)
        self.height = float(height)
        self.thick = float(thick)


    def turn_on_off(self):
        #self.turnonoff=turnonoff       
        if self.buttons == "*":
            self.turnonoff = True
        elif self.buttons == "/":
            self.turnonoff = False
        else:
            self.turnonoff = False
        return self.turnonoff

    
    def change_channel(self,changechannel):
        self.changechannel=changechannel
        if self.buttons == "1":
            self.changechannel = "Canal de Noticias"
        elif self.buttons == "2":
            self.changechannel = "Canal de Desenhos"
        else:
            self.changechannel = "Nenhum Canal"
    

    def volume(self,turnupdown):
        self.turnupdown= turnupdown
        if self.buttons == "+":
            self.turnupdown = True
        elif self.buttons == "-":
            self.turnupdown = False


