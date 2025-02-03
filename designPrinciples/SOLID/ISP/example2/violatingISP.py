from abc import ABC, abstractmethod


class CreditCardPayment(ABC):
    @abstractmethod
    def process_credit_card(self, amount):
        ...

    @abstractmethod
    def process_pay_pall(self, amount):
        ...
      
    @abstractmethod
    def process_bitcoin(self, amount):
        ...


class CreditCardProcessor(CreditCardPayment):
    def process_credit_card(self, amount):
        print(f"processing payment with a credit card for ${amount}")
    
    def process_pay_pall(self, amount):
        raise NotImplementedError("PayPall is not supported!")
    
    def process_bitcoin(self, amount):
        raise NotImplementedError("Bitcoin is not supported!")


if __name__ == "__main__":
    processor = CreditCardProcessor()
    processor.process_credit_card(110.2)
    
    processor.process_pay_pall(110.2) # STDERR: NotImplementedError. 


# This module violated the ISP because: \
# 1. The interface design is logically incorrect. 
# 2. It forces concrete classes implement method they do not need, \
# therefore, clients make dummy implementations.  
# Additionally, this module violates the OCP. 
# See 'example2/complyingISP.py' to fix.  