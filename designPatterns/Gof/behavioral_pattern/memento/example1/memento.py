"""
This modules implements the Memento design pattens.
"""


# 1. Create the 'Memento'
class TextMemento:
    """
    This class represents 'Memento'. \
    An object that stores the 'Originator' state.
    """

    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


# 2. Create the 'Originator'
class TextEditor:
    """
    This class represents the 'Originator' object. \
    An object that saves its state to a Memento object, also is able to \
    restore its previous state from the Memento object.
    """

    def __init__(self):
        self._text = ""  # The state that is saved.

    def write(self, text):
        self._text += text

    def save_state(self):
        return TextMemento(self._text)

    def restore(self, memento: TextMemento):
        self._text = memento.get_state()

    def show_text(self):
        return self._text


# 3. Create a 'Caretaker'
class HistoryManager:
    """
    This class represents the 'Caretaker'. The 'Caretaker' is a object that \
    manages Mementos (e.g., stores them), and implements such operations as \
    'undo()'.
    """

    def __init__(self):
        self._history = []  # Stores Mementos here

    def save(self, memento: TextMemento):
        self._history.append(memento)

    def undo(self):
        if self._history:
            return self._history.pop()

        return None  # No previous state


# Client code
if __name__ == "__main__":
    # 1. Instantiate the 'Originator'
    editor = TextEditor()

    # 2. Instantiate the 'Caretaker'
    history = HistoryManager()

    # Usage
    editor.write("Hello")
    history.save(editor.save_state())  # Save state

    print(editor.show_text())  # STDOUT: Hello

    editor.write(" World")

    print(editor.show_text())  # STDOUT: Hello World

    editor.restore(history.undo())  # Restore state

    print(editor.show_text())  # STDOUT: Hello
