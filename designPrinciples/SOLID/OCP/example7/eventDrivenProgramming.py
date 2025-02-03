from typing import Callable


class EventManager:
    # Observable
    def __init__(self):
        self._listener_list = []

    def register(self, listener: Callable) -> None:
        """Register new listeners (observers) to the 'EventManager'."""
        self._listener_list.append(listener)
    
    def fire_event(self, message) -> None:
        """This function simulates some event happened."""
        for listener in self._listener_list:
            listener(message)


# Example of listeners (observers)
def user1(message):
    print(f"User #1 got new message: '{message}'")

def user2(message):
    print(f"User #2 got new message: '{message}'")


if __name__ == "__main__":
    event_manager = EventManager()
    event_manager.register(user1)
    event_manager.register(user2)

    event_manager.fire_event("Hello")


# This module adheres to the OCP because it allows to add \
# new functionality by creating new listeners and inject \
# this new functionality into existing code 'EventManager' \
# without modifying the existing code.  