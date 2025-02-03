from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def send(self, recipient, message):
        ...


class EmailService(Service):
    def send(self, recipient, message):
        print(f"Send message to '{recipient}': {message}")


class NotificationCenter:
    def __init__(self, email_service: Service): # The '__init__' method is a constructor (or initializer) method. 
        self.email_service = email_service
    
    def notify(self, recipient, message):
        self.email_service.send(recipient, message)


if __name__ == "__main__":
    center = NotificationCenter(EmailService()) # The 'EmailService' is injected right into the constructor method.  

    center.notify("me@chabrovs.tech", "Hello")


# The module adheres to the DIP because the high-level component \
# 'NotificationCenter' does not depend on a concrete implementation of \
# a service.
# The dependency for the high-level component was creates outside of the component \
# and then injected to the constructor method of the dependent component.
# P.S. Aggregation.  