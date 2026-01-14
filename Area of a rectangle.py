class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# Taking input from the user
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Creating an object of the class
rect = Rectangle(length, breadth)

# Displaying the area
print("The area of the rectangle is:", rect.area())
