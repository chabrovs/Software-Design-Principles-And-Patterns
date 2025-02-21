"""
This class implements the State design pattern without state able to \
change the Context (Main Object)'s state on its own, thus the state is \
set only once.
"""


from abc import ABC, abstractmethod


class UserState(ABC):
    """
    This class represents the 'State Interface (or Abstract State)'
    """

    @abstractmethod
    def access_dashboard(self):
        ...


class AnonymousUser(UserState):
    """
    This class represents the 'Concrete State'
    """

    def access_dashboard(self):
        print("Access denied! Authenticate")


class AuthenticatedUser(UserState):
    """
    This class represents the 'Concrete State'
    """

    def access_dashboard(self):
        print("Welcome to the dashboard")


class AdminUser(UserState):
    """
    This class represents the 'Concrete State'
    """

    def access_dashboard(self):
        print("Welcome to the Admin dashboard")


class User:
    """
    This class represents the 'Context (or Main Object)'
    """

    def __init__(self):
        self._state = None

    def set_state(self, state: UserState):
        self._state = state

    def access_dashboard(self):
        self._state.access_dashboard()


# Client code
if __name__ == "__main__":
    user = User()
    user.set_state(AnonymousUser())
    user.set_state(AuthenticatedUser())
    user.access_dashboard()
