class Order:
    def __init__(self):
        self.is_valid = True
        self.id = 123


def process_order(order):
    # Validation logic (business logic | business rule #1).
    if not order.is_valid:
        raise ValueError("Invalid order!")

    # Save order to the database (business logic | business rule #2).
    print("Order saved to the database.")

    # Send conformation email (business logic | business rule #3).
    print("Confirmation email send.")


if __name__ == "__main__":
    my_order = Order()
    process_order(my_order)


# This is an anti-pattern. 