class Order:
    def __init__(self):
        self.is_valid = True
        self.id = 123


def validate_order(order):
    # Business rule #1.
    if not order.is_valid:
        raise ValueError("Invalid order!")


def save_order(order):
    # Business rule #2.
    print("Order saved to the database.")


def send_conformation(order):
    # Business rule #3.
    print("Confirmation email send.")


def process_order(order):
    validate_order(order)
    save_order(order)
    send_conformation(order)


if __name__ == "__main__":
    my_order = Order()
    process_order(my_order)

# This is a correct adherence to the SRP. 