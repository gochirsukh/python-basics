class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

if __name__ == "__main__":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    rectangle = Rectangle(length, width)
    area = rectangle.calculate_area()

    print(f"The area of the rectangle is: {area}")
