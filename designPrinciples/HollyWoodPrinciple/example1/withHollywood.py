from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount):
        ...


class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        print(f"Processing payment via PayPal for ${amount}")


class Framework:
    def execute(self, processor: PaymentProcessor, amount: int):
        print("Framework is controlling the flow")
        processor.process(amount)

    
if __name__ == "__main__":
    framework = Framework()
    processor = PayPalProcessor()

    framework.execute(processor, 10)
