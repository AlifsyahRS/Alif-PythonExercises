import math


class Shape:
    def __init__(self, color="green", filled=True):
        self.color = color
        self.filled = filled

    def __str__(self):
        return f"Shape with color = {self.color}, filled = {self.filled}"

    def getColor(self):
        return self.color

    def setColor(self, new_color):
        self.color = new_color

    def isFilled(self):
        return self.filled

    def setFilled(self, new_bool):
        self.filled = new_bool


class Circle(Shape):
    def __init__(self, color, filled, radius=1.0):
        self.color = color
        self.filled = filled
        Shape.__init__(self, self.color, self.filled)
        self.radius = radius

    def __str__(self):
        return f"{super().__str__()}, radius = {self.getRadius()}".replace("Shape", "Circle")

    def getRadius(self):
        return float(self.radius)

    def setRadius(self, new_radius):
        self.radius = new_radius

    def getArea(self):
        return (self.getRadius() ** 2) * math.pi

    def getPerimeter(self):
        return self.getRadius() * 2 * math.pi


class Rectangle(Shape):
    def __init__(self, color, filled, length, width):
        self.color = color
        self.filled = filled
        Shape.__init__(self, self.color, self.filled)
        self.length = length
        self.width = width

    def __str__(self):
        return f"{super().__str__()}, length = {self.getLength()}, width = {self.getWidth()}".replace("Shape", "Rectangle")

    def getLength(self):
        return float(self.length)

    def setLength(self, new_length):
        self.length = new_length

    def getWidth(self):
        return float(self.width)

    def getArea(self):
        return self.getLength() * self.getWidth()

    def getPerimeter(self):
        return (2 * self.getLength()) + (2 * self.getWidth())


class Square(Rectangle):
    def __init__(self, color, filled, sides=1.0):
        self.color = color
        self.filled = filled
        self.sides = sides
        Rectangle.__init__(self, self.color, self.filled,
                           self.sides, self.sides)

    def __str__(self):
        return f"{super().__str__()}".replace("Rectangle", "Square").replace(f"length = {self.getSides()}, width = {self.getSides()}", f"sides = {self.getSides()}")

    def getSides(self):
        return float(self.sides)

    def setSides(self, new_sides):
        self.sides = new_sides


my_circle = Circle("red", True, 1.0)
my_rectangle = Rectangle("blue", False, 5.0, 6.0)
my_square = Square("green", True, 3.0)


def main():
    print(my_circle.getColor())
    print(my_circle.__str__(), end='.\n')
    print(my_circle.getArea())
    print(my_circle.getPerimeter())
    print(my_rectangle.__str__(), end='.\n')
    print(my_rectangle.getArea())
    print(my_rectangle.getPerimeter())
    print(my_square.__str__(), end='.\n')
    print(my_square.getArea())
    print(my_square.getPerimeter())


if __name__ == "__main__":
    main()
