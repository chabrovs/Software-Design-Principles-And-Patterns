class MySQLDatabase:
    def save_order(self, order):
        print(f"Saving order to MySQL '{order}'")


class OrderService:
    def __init__(self):
        self.database = MySQLDatabase() # Violation: Direct dependency on low-level module. 
    
    def process_order(self, order):
        print(f"Processing order")
        self.database.save_order(order)


if __name__ == "__main__":
    order_service = OrderService()
    order_service.process_order(1)


# This module violate the DIP because the high-level module 'OrderService' \ 
# implementing business logic has direct dependency on low-level module \
# 'MySQLDatabase' implementing database details. 
# See 'example1/complyingDIP.py' to fix.  