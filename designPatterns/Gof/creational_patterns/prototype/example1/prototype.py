"""
This module implements Prototype via inheritance.
"""


import copy


class Prototype:
    """This class implements the copying mechanism."""
    def clone(self):
        return copy.deepcopy(self)


class User(Prototype):
    """This is a concrete prototype class."""
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Username: {self.name}, Email: {self.email}"


# Usage
if __name__ == "__main__":
    user1 = User("Sergei", "me@chabrovs.tech")
    user2 = user1.clone()

    user2.name = "John"

    print(user1) # STDOUT: Username: Sergei, Email: me@chabrovs.tech
    print(user2) # STDOUT: Username: John, Email: me@chabrovs.tech
