class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def area(self):
        print(f"Area of square: {self.width * self.width}")

    def __str__(self):
        return f"Square(color={self.color}, is_filled={self.is_filled}, width={self.width})"
    
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def area(self):
        print(f"Area of circle: {3.14 * self.radius * self.radius}")

    def __str__(self):
        return f"Circle(color={self.color}, is_filled={self.is_filled}, radius={self.radius})"
    
square = Square("red", True, 5)
circle = Circle("blue", False, 3)
square.area()
circle.area()
print(square)
print(circle)
