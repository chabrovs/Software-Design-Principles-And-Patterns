from abc import ABC, abstractmethod
from decimal import Decimal


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: Decimal) -> None:
        ...


class StripeGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing Stripe payment for ${amount} $")


class PayPalGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing PayPal payment for ${amount}")


class PaymentService:
    def __init__(self, gateway: PaymentGateway): # Dependency inversion and Dependency injection. 
        self._gateway = gateway # Access modification.  
    
    def process_payment(self, amount):
        self._gateway.process_payment(amount)


if __name__ == "__main__":
    payment_service = PaymentService(PayPalGateway())
    payment_service.process_payment(100.12)