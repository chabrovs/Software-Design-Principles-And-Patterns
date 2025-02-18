"""
This module implements the command design pattern with Undo functionality.
"""


from abc import ABC, abstractmethod


# 1. Crete a 'Command Interface'
class UndoableCommand(ABC):
    """
    This module represents the 'Command Interface'.
    """

    @abstractmethod
    def execute(self):
        ...

    @abstractmethod
    def undo(self):
        ...


# 2. Crete a 'receiver'
class TextEditor:
    """
    This class represents the 'Receiver' object.
    """

    def __init__(self):
        self.text = ""

    def write(self, text: str):
        self.text += text

    def erase(self):
        self.text = self.text[:-1]

    def show_text(self):
        return self.text

# 3. Create 'Concrete Commands'


class WriteCommand(UndoableCommand):
    """
    This class represents a 'Concrete Command' object.
    """

    def __init__(self, editor: TextEditor, text: str):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.write(self.text)

    def undo(self):
        for _ in self.text:
            self.editor.erase()


# 4. Create an 'Invoker'
class CommandHistory:
    """
    This class represents the 'Invoker'.
    """

    def __init__(self):
        """
        The 'Invoker' stores all previously executed command in a list.
        """

        self.history = []

    def execute_command(self, command: UndoableCommand):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()


# Client code
if __name__ == "__main__":
    # 1. Instantiate the 'Receiver'.
    editor = TextEditor()

    # 2. Instantiate the 'Invoker (sender)'.
    history = CommandHistory()

    # 3. Instantiate 'Concrete Commands'.
    write1 = WriteCommand(editor, "Hello")
    write2 = WriteCommand(editor, " World")
    write3 = WriteCommand(editor, " !")

    # Usage:
    [history.execute_command(command) for command in [write1, write2, write3]]

    print(editor.show_text())  # STDOUT: Hello World !

    history.undo_last_command()
    history.undo_last_command()

    print(editor.show_text())  # STDOUT: Hello
