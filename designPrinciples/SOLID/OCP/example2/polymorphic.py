from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, amount: float) -> float:
        ...


class RegularDiscount(DiscountStrategy):
    def calculate(self, amount):
        return round(amount * 0.1, 2)
    

class PremiumDiscount(DiscountStrategy):
    def calculate(self, amount):
        return round(amount * 0.2, 2)
    

if __name__ == "__main__":
    discount_strategy = RegularDiscount()
    
    print(discount_strategy.calculate(110.2))

    discount_strategy2 = PremiumDiscount()

    print(discount_strategy.calculate(110.2))