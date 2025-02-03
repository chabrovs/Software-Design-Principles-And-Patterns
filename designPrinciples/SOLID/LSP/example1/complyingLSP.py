from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return area of a shape."""


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    

if __name__ == "__main__":
    rect = Rectangle(4, 5)
    print(rect.area())

    sq = Square(4)
    print(sq.area())


# This module adheres to the LSP because the \
# hierarchy in build upon abstraction 'Shape'.  

