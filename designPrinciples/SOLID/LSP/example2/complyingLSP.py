from abc import ABC, abstractmethod


class Bird(ABC):
    pass


class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        ...


class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow is flying...")


class Penguin(Bird):
    def swim(self):
        print("Penguin is swimming...")


def make_bird_fly(bird: FlyingBird):
    bird.fly() # No need in explicit type checks. 


if __name__ == "__main__":
    sparrow = Sparrow()
    make_bird_fly(sparrow)

    penguin = Penguin()
    make_bird_fly(penguin) # STDERROR: AttributeError: 'Penguin' object has no attribute 'fly'



# This module adheres to the LSP because \
# 1. There are not logical error in the class hierarchy. 
# 2. Usage of the subclasses does not require a typecheck. 
# To fix this issue we have created an additional \
# abstraction layer.