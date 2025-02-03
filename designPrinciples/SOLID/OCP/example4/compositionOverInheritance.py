class Notification:
    def send(self, message):
        print(f"Base notification: '{message}'")


class EmailNotification:
    def __init__(self, notification):
        self.notification = notification
    
    def send(self, message):
        self.notification.send(message)
        print("Email: '{message}'")


class SMSNotification:
    def __init__(self, notification):
        self.notification = notification
    
    def send(self, message):
        self.notification.send(message)
        print("SMS: '{message}'")


if __name__ == "__main__":
    # Dynamic composition
    base = Notification()
    email = EmailNotification(base)
    sms = SMSNotification(email)

    sms.send("Hello")


# This module adheres to the OCP because it allows \ 
# to add new functionality without changing existing code.  