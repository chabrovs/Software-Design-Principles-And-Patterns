class NotificationService:
    def send_notification(self, message):
        print(f"Notification send: {message}")


class OrderProcessor:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service
    
    def process_order(self, order):
        print("Processing order...")
        self.notification_service.send_notification(f"Processing order: '{order}'")


if __name__ == "__main__":
    notification_service = NotificationService()
    order_processor = OrderProcessor(notification_service)

    order_processor.process_order({"id": 1})


# This module adheres to the SRP because the additional unrelated responsibility 
# such as sending notification has been injected to the 'OrderProcessor' class 
# from the outer scope. Thank to which, the 'OrderProcessor' is not overloaded with
# unrelated responsibilities.  