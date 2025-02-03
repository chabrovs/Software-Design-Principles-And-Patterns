from abc import ABC, abstractmethod


class CreditCardPayment(ABC):
    @abstractmethod
    def process_credit_card(self, amount):
        ...

class PayPalPayment(ABC):
    @abstractmethod
    def process_paypal(self, amount):
        ...

class BitcoinPayment(ABC):
    @abstractmethod
    def process_bitcoin(self, amount):
        ...


class CreditCardProcessor(CreditCardPayment):
    def process_credit_card(self, amount):
        print(f"Processing Payment with Credit Card for ${amount}")


class PayPalProcessor(PayPalPayment):
    def process_paypal(self, amount):
        print(f"Processing Payment with PayPal for ${amount}")


if __name__ == "__main__":
    credit_card_processor = CreditCardProcessor()
    credit_card_processor.process_credit_card(110.2)


# This module complies with the ISP and OCP. 