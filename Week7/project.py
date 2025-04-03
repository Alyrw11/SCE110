import math
  
def calculate_square_area(side_length):
    return side_length * side_length
def calculate_rectangle_area(length, width):
    return length * width
def calculate_circle_area(radius):
    return math.pi * radius * radius


shape = ""

while shape != "exit":
    shape = input("Enter the shape (square, rectangle, circle) or 'exit' to quit: ").lower()
    if shape == "square":
        side_length = float(input("Enter the side length of the square: "))
        area = calculate_square_area(side_length)
        print(f"The area of the square is {area}")
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is {area}")
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle is {area}")
    elif shape != "exit":
        print("Invalid shape. Please try again.")