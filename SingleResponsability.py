# This is the implementation when the responsabilities are divided.

from datetime import datetime

class Order:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.order_date = datetime.now()

class OrderCalculator:
    @staticmethod
    def calculate_total(order):
        return sum(item['price'] * item['quantity'] for item in order.items)

class OrderPrinter:
    @staticmethod
    def print_order(order):
        print(f"Order ID: {order.order_id}")
        print(f"Customer: {order.customer_name}")
        print(f"Date: {order.order_date}")
        print("Items:")
        for item in order.items:
            print(f"  - {item['name']}: ${item['price']} x {item['quantity']}")
        print(f"Total: ${OrderCalculator.calculate_total(order)}")

class OrderSaver:
    @staticmethod
    def save_to_database(order):
        # This is a mock implementation
        print(f"Saving order {order.order_id} to database...")
        # In a real scenario, this would interact with a database

# Usage
if __name__ == "__main__":
    order = Order(
        "12345",
        "John Doe",
        [
            {"name": "Book", "price": 10.99, "quantity": 2},
            {"name": "Pen", "price": 1.99, "quantity": 5}
        ]
    )

    OrderPrinter.print_order(order)
    OrderSaver.save_to_database(order)
