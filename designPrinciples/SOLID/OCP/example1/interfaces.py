from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        ...

class EmailSender(NotificationSender):
    def send(self, message):
        print(f"Send message: '{message}'")


class SMSSender(NotificationSender):
    def send(self, message):
        print(f"Send message: '{message}'")


if __name__ == "__main__":
    email_sender = EmailSender()
    email_sender.send("Hello")

    sms_sender = SMSSender()
    sms_sender.send("Hello SMS")


# This module adheres the OCP because the 'NotificationSender' interface \
# (abstract base class) allows extension of functionality by new adding concrete classes \
# that implement the interface without modifying the code of existing classes. 