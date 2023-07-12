class Rectangle():


    def __init__(self):
        self.width = 0
        self.height = 0
    

    def side_change(self,newwidth,newheight):
        self.width = newwidth
        self.height = newheight
    

    def side_show(self):
        print("{:.2f}\n{:.2f}".format(self.width,self.height))
    

    def area_per_calc(self):
        self.area = self.width * self.height
        self.per = (self.width * 2) + (self.height * 2)
        print("{:.2f}\n{:.2f}".format(self.area,self.per))


    def baseboard(self):
        self.base = self.area*0.15
        print(self.base)
