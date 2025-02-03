from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        ...


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment for ${amount} via PayPal")


class BankProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment for ${amount} via Bank")


def process_order(payment_processor: PaymentProcessor, amount: float):
    instance = payment_processor

    if isinstance(instance, PayPalProcessor): # Violation LSP: Explicit subclass check.
        print("Processing via PayPal")
    elif isinstance(instance, BankProcessor): # Violation LSP: Explicit subclass check.
            print("Processing via Back")
    else:
        raise ValueError("Payment processor in not supported.")

    instance.process_payment(amount)


if __name__ == "__main__":
    processor = PayPalProcessor()
    process_order(processor, 110.2)


# This module violated both LSP and OCP. \
# Each time a new payment method is introduced \
# the 'process_order' function must be modified.  