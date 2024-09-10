# Overriding ex 2
import math


class Shape:
    def area(self):
        print("Area of the Shape")


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        print(math.pi * math.pow(self.a, self.b))


cir = Circle(10, 2)
rect = Rectangle(10, 2)
cir.area()  # Overridden implementation of Circle area
print(rect.area())  # Overridden implementation of Rectangle area
