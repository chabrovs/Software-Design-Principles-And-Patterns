"""
This module implements and represents a simple template of \
the Observer pattern with a Push-Based changed state propagation model.
"""


from abc import ABC, abstractmethod


class Observer(ABC):
    """
    This class represents the 'Observer Interface (or Abstract Observer)'
    """

    @abstractmethod
    def update(self, state):
        ...


class Subject:
    """
    This class represents a 'Subset (or Observable)'
    """

    def __init__(self):
        """
        The state of an object and list of Observers are stored here.
        """

        self._observer_list: list[Observer] = []
        self._state = None

    def attach(self, observer: Observer):
        """
        Add new observer.
        """

        self._observer_list.append(observer)

    def detach(self, observer: Observer):
        """
        Remove an observer from the 'observer_list'
        """

        self._observer_list.remove(observer)

    def notify_observers(self):
        """
        Based on the Push-Based propagation model - set the new state \
        to all the observers.
        """

        for observer in self._observer_list:
            observer.update(self._state)

    def set_state(self, new_state):
        """
        The 'Subject' must implement a setter method to set a new state. \
        Whenever a new state is set - Observers from the 'observer_list' \
        must get the newest state (based on the Push-Based model).
        """

        self._state = new_state
        self.notify_observers()


class ConcreteObserver1(Observer):
    """
    This class represents a 'ConcreteObserver'
    """

    def update(self, state):
        print(f"Observer 1 state change to: '{state}'")


class ConcreteObserver2(Observer):
    """
    This class represents a 'ConcreteObserver'
    """

    def update(self, state):
        print(f"Observer 2 state change to: '{state}'")


# Client code
if __name__ == "__main__":
    # 1. Create observers
    observer1 = ConcreteObserver1()
    observer2 = ConcreteObserver2()

    # 2. Create 'Subject (Observable)'
    observable = Subject()

    # 3. Attach observers to the 'Subject'
    [observable.attach(observer) for observer in [observer1, observer2]]

    # Usage (change state of the Subject).
    observable.set_state("Hello new State")
