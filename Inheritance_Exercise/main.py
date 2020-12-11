from Shape import Circle, Rectangle, Square

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
