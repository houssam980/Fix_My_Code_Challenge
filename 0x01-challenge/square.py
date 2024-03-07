#!/usr/bin/python3

class Square:
   
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def calculate_area(self):
  
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{self.width}/{self.height}" 

if __name__ == "__main__":
    square = Square(width=12, height=9)
    print(square)
    print(square.calculate_area())
    print(square.calculate_perimeter())

