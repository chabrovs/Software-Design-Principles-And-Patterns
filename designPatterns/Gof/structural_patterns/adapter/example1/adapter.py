"""
Adapter Pattern Example 1. \
This is the Class-Based Adapter using Inheritance.
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


class Adapter(Target, OldSystem):
    """
    The intermediary class between the 'Target interface' and the \
    'OldSystem'.
    """

    def request(self):
        return self.specific_request()


# Usage (client code).
if __name__ == "__main__":
    adapter = Adapter()
    print(adapter.request())  # STDOUT: Response from the Old System.
