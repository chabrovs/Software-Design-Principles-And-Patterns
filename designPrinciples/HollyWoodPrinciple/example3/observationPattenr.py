from abc import ABC, abstractmethod


class Observable:
    # Push-Based. Change Propagation. 

    def __init__(self):
        self.data = 1
        self._observer_list = [] # Contains all entities that observe (follow) this Observable subject.  

    def subscribe(self, observer):
        """This function adds new observers to the list of all observers."""
        self._observer_list.append(observer)
        self.notify()

    def notify(self):
        print("The observable notifies all observers that a change has been made.")

        for observer in self._observer_list:
            observer.update_data(self.data)
    
    def set_data(self, new_data):
        self.data = new_data
        self.notify()


class ObserverI(ABC):
    def __init__(self):
        self.current_data: None | int

    @abstractmethod
    def update_data(self, new_data):
        """Setter method to update the observers current data."""
        ...

    @abstractmethod
    def get_data(self):
        """Getter methods to check the observers current data."""
        ...


class Observer(ObserverI):
    def __init__(self):
        super().__init__()
        self.current_data = None

    def update_data(self, new_data):
        self.current_data = new_data

    def get_data(self):
        return self.current_data
    

if __name__ == "__main__":
    # instantiate observable  
    subject = Observable()

    # instantiate observers
    observer1 = Observer()
    observer2 = Observer()

    # Check current observers data.
    print(observer1.get_data()) # STDOUT: None
    print(observer2.get_data()) # STDOUT: None

    # Subscribe (attach) observers to the observable subject. 
    subject.subscribe(observer1)
    subject.subscribe(observer2)

    # Check current observers data now. 
    print(observer1.get_data()) # STDOUT: 1
    print(observer2.get_data()) # STDOUT: 1

    # Update the observable data. 

    subject.set_data(555)


    # Check observant1 and observant2 current data. 
    
    print(observer1.get_data()) # STDOUT: 555
    print(observer2.get_data()) # STDOUT: 555



    