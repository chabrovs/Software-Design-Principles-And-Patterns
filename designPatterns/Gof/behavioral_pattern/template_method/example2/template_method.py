"""
This module implement the Template Method design pattern.
"""


from abc import ABC, abstractmethod


class Game(ABC):
    """
    This class represents the 'Abstract Class (Template Class)'
    """

    def run(self):
        self.initialize()

        while not self.is_game_over():
            self.update()
            self.render()
        self.cleanup()

    @abstractmethod
    def initialize(self):
        ...

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def render(self):
        ...

    @abstractmethod
    def is_game_over(self):
        ...

    def cleanup(self):
        print(f"\n"*10)


class MyGame(Game):
    """
    This class represents 'Concrete Class'
    """

    def initialize(self):
        print("Game started")

    def update(self):
        print("->>")

    def render(self):
        print("render")

    def is_game_over(self):
        return True


# Client code
if __name__ == "__main__":
    game = MyGame()
    game.run()