"""
This module implement the command design pattern.
"""


from abc import ABC, abstractmethod


class Command(ABC):
    """
    This is the 'Command Interface'
    """

    @abstractmethod
    def execute(self):
        ...


class Server:
    """
    This class represents the Receiver. 
    """

    def turn_on(self):
        return "The Server is ON"

    def turn_of(self):
        return "The Server is OFF"


class ServerOnCommand(Command):
    """
    This class represents the 'Concrete Command'.
    """

    def __init__(self, server: Server):
        self.server = server

    def execute(self):
        return self.server.turn_on()


class ServerOffCommand(Command):
    """
    This class represents the 'Concrete Command'.
    """

    def __init__(self, server: Server):
        self.server = server

    def execute(self):
        return self.server.turn_of()


class RemoteServerController:
    """
    This class represents the Invoker.
    """

    def __init__(self):
        self.command = None  # Stores the command

    def set_command(self, command: Command):
        self.command = command

    def execute(self):
        return self.command.execute()


# Client code
if __name__ == "__main__":
    # 1. Instantiate the 'Receiver'.
    server = Server()

    # 2. Instantiate the 'Commands'.
    server_on = ServerOnCommand(server)
    server_of = ServerOffCommand(server)

    # 3. Instantiate
    remote_controller = RemoteServerController()

    # 3.1 Set the command to the 'Controller'
    remote_controller.set_command(server_on)

    # 4. Execute the command

    print(remote_controller.execute())
