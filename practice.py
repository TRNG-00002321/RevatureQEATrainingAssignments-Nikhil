import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return (self.b * self.h) / 2

circle = Circle(89)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

print(f"Area of Circle: {circle.area():.2f}")
print(f"Area of Rectangle: {rectangle.area():.2f}")
print(f"Area of Triangle: {triangle.area():.2f}")