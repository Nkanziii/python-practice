class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False

r = Rectangle(4, 6)
print(r.area())
print(r.perimeter())
print(r.is_square())

s = Rectangle(5, 5)
print(s.is_square())