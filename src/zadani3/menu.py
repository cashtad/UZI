import math

shape = input("Choose geometric shape (triangle/rectangle/circle) or type 'exit' to leave program: ")
match shape:
    case 'exit':
        exit()
    case 'rectangle':
        a = int(input("First side length: "))
        b = int(input("Second side length: "))
        result = a*b
        print(f"Area of rectangle is: {result}")
    case 'circle':
        a = int(input("Radius: "))
        result = a*a*math.pi
        print(f"Area of circle is: {result}")
    case 'triangle':
        a = int(input("Base length: "))
        b = int(input("Height: "))
        result = a * b * 0.5
        print(f"Area of triangle is: {result}")
