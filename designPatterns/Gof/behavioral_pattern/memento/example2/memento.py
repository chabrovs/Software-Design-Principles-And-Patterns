"""
This module implements the Memento patters were the memento is a \
state of the game, and the 'SaveManager' is the caretaker.
"""


class GameMemento:
    def __init__(self, level, health):
        self.level = level
        self.health = health


class Game:
    """
    This class represents the 'Originator'.
    """

    def __init__(self):
        """
        The state of the game is represented by 'level' and 'health'
        """

        self.level = 1
        self.health = 100

    def play(self):
        self.level += 1
        self.health -= 10

    def save(self):
        return GameMemento(self.level, self.health)

    def restore(self, state: GameMemento):
        self.level = state.level
        self.health = state.health

    def show_status(self):
        return f"Status: level='{self.level}', health='{self.health}'"


class SaveManager:
    def __init__(self):
        self._save_list = []

    def save_game(self, memento: GameMemento):
        self._save_list.append(memento)

    def load_save(self):
        if self._save_list:
            return self._save_list.pop()

        return None


# Client code
if __name__ == "__main__":
    # 1. Instantiate 'Originator'
    game = Game()

    # 2. Instantiate 'Caretaker'
    save_manager = SaveManager()

    # Usage
    print(game.show_status())  # STDOUT Status: level='1', health='100'
    save_manager.save_game(game.save())

    game.play()

    print(game.show_status())  # STDOUT: Status: level='2', health='90'

    game.restore(save_manager.load_save())
    print(game.show_status())  # STDOUT: Status: level='1', health='100'
