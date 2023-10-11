class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._pi = 3.141  

    def calculate_area(self):
        area = self._pi * (self.radius ** 2)
        return area

    def calculate_circumference(self):
        circumference = 2 * self._pi * self.radius
        return circumference
circle = Circle(5)

print(f"Area of the circle: {circle.calculate_area()}")
print(f"Circumference of the circle: {circle.calculate_circumference()}")

