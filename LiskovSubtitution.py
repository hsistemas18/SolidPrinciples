from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Order(ABC):
    def __init__(self, order_id, customer_name, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_amount = total_amount
        self.order_date = datetime.now()

    @abstractmethod
    def calculate_shipping(self):
        pass

    @abstractmethod
    def get_delivery_date(self):
        pass

    def process(self):
        shipping_cost = self.calculate_shipping()
        delivery_date = self.get_delivery_date()
        return f"Order {self.order_id} for {self.customer_name}:\n" \
               f"Total: ${self.total_amount:.2f}\n" \
               f"Shipping: ${shipping_cost:.2f}\n" \
               f"Delivery Date: {delivery_date.strftime('%Y-%m-%d')}"

class StandardOrder(Order):
    def calculate_shipping(self):
        return self.total_amount * 0.1  # 10% of total for standard shipping

    def get_delivery_date(self):
        return self.order_date + timedelta(days=5)  # Standard delivery in 5 days

class ExpressOrder(Order):
    def calculate_shipping(self):
        return self.total_amount * 0.2  # 20% of total for express shipping

    def get_delivery_date(self):
        return self.order_date + timedelta(days=2)  # Express delivery in 2 days

class InStorePickupOrder(Order):
    def calculate_shipping(self):
        return 0  # No shipping cost for in-store pickup

    def get_delivery_date(self):
        return self.order_date + timedelta(days=1)  # Available for pickup next day

def process_order(order: Order):
    return order.process()

# Usage
if __name__ == "__main__":
    standard_order = StandardOrder("SO001", "John Doe", 100)
    express_order = ExpressOrder("EO001", "Jane Smith", 150)
    pickup_order = InStorePickupOrder("PO001", "Alice Johnson", 75)

    orders = [standard_order, express_order, pickup_order]

    for order in orders:
        print(process_order(order))
        print()
