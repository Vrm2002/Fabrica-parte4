from shape import Shape


class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()


        self.width = width
        self.length = length


    def area(self):


        result = self.width * self.length
        return result