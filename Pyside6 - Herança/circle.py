from shape import Shape


class Circle(Shape):
    def __init__(self,radius):
        super().__init__()


        self.radius = radius


    def area(self):


        result = 3.14*(self.radius**2)
        return result