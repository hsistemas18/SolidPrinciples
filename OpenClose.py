from abc import ABC, abstractmethod

class Order:
    def __init__(self, id, customer, total_amount):
        self.id = id
        self.customer = customer
        self.total_amount = total_amount

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order):
        pass

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, order):
        return order.total_amount * 0.05  # 5% discount

class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, order):
        return order.total_amount * 0.10  # 10% discount

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, order):
        return order.total_amount * 0.15  # 15% discount

class OrderProcessor:
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy

    def process_order(self, order):
        discount = self.discount_strategy.apply_discount(order)
        final_amount = order.total_amount - discount
        return final_amount

# Usage
if __name__ == "__main__":
    regular_order = Order("RO001", "John Doe", 100)
    premium_order = Order("PO001", "Jane Smith", 200)
    vip_order = Order("VO001", "Alice Johnson", 300)

    regular_processor = OrderProcessor(RegularDiscount())
    premium_processor = OrderProcessor(PremiumDiscount())
    vip_processor = OrderProcessor(VIPDiscount())

    print(f"Regular Order Final Amount: ${regular_processor.process_order(regular_order):.2f}")
    print(f"Premium Order Final Amount: ${premium_processor.process_order(premium_order):.2f}")
    print(f"VIP Order Final Amount: ${vip_processor.process_order(vip_order):.2f}")
