from typing import Callable


class EventManager:
    def __init__(self):
        self.listener_list = []

    def register(self, listener: Callable) -> None:
        self.listener_list.append(listener)

    def fire_event(self, event_data) -> None:
        for listener in self.listener_list:
            listener.handler_event(event_data)


class Listener:
    def handler_event(self, event_data) -> None:
        print(f"Handling event with data '{event_data}'")


if __name__ == "__main__":
    event_manager = EventManager()
    listener1 = Listener()

    event_manager.register(listener1)
    
    event_manager.fire_event({"type": "user_logged_in", "user": "Sergei"})