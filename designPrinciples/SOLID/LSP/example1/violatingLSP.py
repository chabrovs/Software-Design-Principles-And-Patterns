from typing import override # For Python > 3.11
# from typing_extensions import override # For Python < 3.11


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height
    

# Violating LSP 
class Square(Rectangle):
    @override # This decorator is used to indicate that the superclass method is being override. (used just for type annotation).  
    def set_width(self, width):
        self.width = self.heigh = width # Breaks superclass's expected behavior.

    @override
    def set_height(self, height):
        self.width = self.height = height # Breaks superclass's expected behavior.


if __name__ == "__main__":
    def print_area(rect: Rectangle):
        rect.set_width(4)
        rect.set_height(5)

        print(rect.area())

    rect = Rectangle(2, 3)
    print_area(rect)

    sq = Square(4, 4)
    print_area(sq)


# This module violates LSP because the subclass 'Square' \
# changes the expected behavior of its superclass 'Rectangle'. \
# Thus, we cannot substitute the 'Rectangle' class with \
# its subclass 'Square'.   
# See 'example1/complyingLSP.py' to see the fix.  