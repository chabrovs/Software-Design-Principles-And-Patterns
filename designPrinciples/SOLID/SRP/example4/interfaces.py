from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    def process_payment(self, amount):
        ...


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Process payment via PayPal for ${amount}")


class BankProcessor(PaymentProcessor):
    def process_payment(self, amount):   
        print(f"Process payment via a Bank for ${amount}")


if __name__ == "__main__":
    PayPalProcessor().process_payment(100)
    BankProcessor().process_payment(200)


# This module adheres to the SRP as each payment responsibility \ 
# has its own class. 
