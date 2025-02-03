from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def fly():
        ...


class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying!")


class Penguin(Bird): # LSP violation: logical hierarchy violation.
    def fly(self):
        print("Penguins cannot fly")


def make_bird_fly(bird: Bird):
    if isinstance(bird, Penguin):
        print("This bird cannot fly!") # LSP Violation: typechecking before subclass usage. 
    else:
        bird.fly()


if __name__ == "__main__":
    sparrow = Sparrow()
    make_bird_fly(sparrow)

    penguin = Penguin()
    make_bird_fly(penguin)


# This module does not adhere to the LSP because \
# 1. Logical error in the class hierarchy. (There is 
# bo need to implement the method if we know beforehand 
# that the method does not align to the entity).\
# 2. Explicit typechecking before subclass usage. 
# See 'example2/complyingLSP.py' the fix.  