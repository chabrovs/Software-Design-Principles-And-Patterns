from typing import Callable


def callbackFunc(data):
    print(f"This callback is executed with data {data}")


class EventManager:
    def __init__(self):
        self.listener_list = []

    def register(self, listener: Callable):
        self.listener_list.append(listener)

    def fire_event(self, event_data):
        print("Event manager calling Listeners")

        for listener in self.listener_list:
            listener(event_data)


if __name__ == "__main__":
    event_manager = EventManager()

    event_manager.register(callbackFunc)

    event_manager.fire_event("Hello")


# In this example the lower-level element is the 'callbackFunc' \
# and the higher-level element responsible for calling the lower-level \
# element (taking the control flow) is the 'EventManager'.
