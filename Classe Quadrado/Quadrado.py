class Square():
    

    def __init__(self,):
        self.sidelen = 0
    

    def show_area(self):
        self.area = self.sidelen**2
        print(self.area)
        print(self.sidelen)
    

    def change_side(self,newside):
        self.sidelen = newside