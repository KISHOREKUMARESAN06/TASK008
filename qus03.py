import math

class Shape:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def area(cls, radius):
        return math.pi * radius ** 2

    @classmethod
    def perimeter(cls, radius):
        return 2 * math.pi * radius

circle = Shape(5)  
area = circle.area(circle.radius)
perimeter = circle.perimeter(circle.radius)

print(f"Circle Area: {area}")
print(f"Circle Perimeter: {perimeter}")

