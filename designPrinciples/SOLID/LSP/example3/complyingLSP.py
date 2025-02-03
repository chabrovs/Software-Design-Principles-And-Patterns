from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        ...
    

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment for ${amount} via PayPal")


class BankProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment for ${amount} via Bank")


def process_payment(processor: PaymentProcessor, amount: float):
    processor.process_payment(amount)


if __name__ == "__main__":
    process_payment(PayPalProcessor(), 110.2)
    process_payment(BankProcessor(), 110.2)

