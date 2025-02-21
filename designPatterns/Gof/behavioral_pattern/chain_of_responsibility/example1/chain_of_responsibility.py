"""
This module implement the CoR design pattern.
"""


from abc import ABC, abstractmethod


class SupportHandler(ABC):
    """
    This is the 'Handler Interface'.
    """

    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

        return handler  # Enables method chaining

    @abstractmethod
    def handle(self, request):
        ...


class Level1Support(SupportHandler):
    """
    This class is a 'Concrete Handler'.
    """

    def handle(self, request):
        if request == "password_reset":
            return "Level 1: Password was reset"
        elif self.next_handler:
            return self.next_handler.handle(request)

        return "Request could not be resolved!"


class Level2Support(SupportHandler):
    """
    This class is a 'Concrete Handler'.
    """

    def handle(self, request):
        if request == "software_issue":
            return "Level 2: Software issue resolved"
        elif self.next_handler:
            return self.next_handler.handle(request)

        return "Request could not be resolved!"


class Level3Support(SupportHandler):
    """
    This class is a 'Concrete Handler'.
    """

    def handle(self, request):
        return f"Level 3: Escalated request handled ({request})"


# Client code
if __name__ == "__main__":
    # 1. Build chain
    level1 = Level1Support()
    level2 = Level2Support()
    level3 = Level3Support()

    # 2. Set the chain up

    level1.set_next_handler(level2).set_next_handler(level3)

    # 3. Usage

    print(level1.handle("password_reset"))
    print(level1.handle("software_issue"))
    print(level1.handle("unknown"))
