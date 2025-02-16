"""
Adapter Pattern Example 2 \
This is the Object-Based Adapter using Composition.
"""


from abc import ABC, abstractmethod


class OldSystem:
    """
    Represents an systems that the client actually wants to use, \
    but cannot due to interface mismatch between the 'Target interface' \
    and the 'OldSystem' interface.
    """

    def specific_request(self):
        return "Response from the Old System."


class Target(ABC):
    """
    This class represents the current interface the client uses.
    """

    @abstractmethod
    def request(self):
        ...


class Adapter(Target):
    """
    The intermediary class between the 'Target interface' and the \
    'OldSystem'.
    """

    def __init__(self, adaptee):
        """Composition using Dependency Injection."""
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()


# Usage (client code).
if __name__ == "__main__":
    old_system = OldSystem()
    adapter = Adapter(old_system)  # Inject dependency 'adaptee'
    print(adapter.request())  # STDOUT: Response from the Old System.
