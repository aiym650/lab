class Shape:
    def __init__ (self):
        self.area = 0
class Square:
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2

shape = Shape()
print(shape.area)

square = Square(30)
print(square.area()) 