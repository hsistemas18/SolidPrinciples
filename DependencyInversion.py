from abc import ABC, abstractmethod

# Abstractions
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class InventoryManager(ABC):
    @abstractmethod
    def update_inventory(self, product_id, quantity):
        pass

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

# Low-level modules (implementations)
class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through Stripe")

class SQLInventoryManager(InventoryManager):
    def update_inventory(self, product_id, quantity):
        print(f"Updating inventory in SQL database: Product {product_id}, Quantity: {quantity}")

class EmailNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")

# High-level module
class OrderProcessor:
    def __init__(self, payment_processor: PaymentProcessor, 
                 inventory_manager: InventoryManager, 
                 notification_service: NotificationService):
        self.payment_processor = payment_processor
        self.inventory_manager = inventory_manager
        self.notification_service = notification_service

    def process_order(self, order):
        # Process payment
        self.payment_processor.process_payment(order.total_amount)

        # Update inventory
        for item in order.items:
            self.inventory_manager.update_inventory(item.product_id, item.quantity)

        # Send notification
        self.notification_service.send_notification(f"Order {order.id} has been processed")

        print(f"Order {order.id} processed successfully")

# Order and OrderItem classes
class OrderItem:
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

class Order:
    def __init__(self, id, items, total_amount):
        self.id = id
        self.items = items
        self.total_amount = total_amount

# Client code
if __name__ == "__main__":
    # Create instances of low-level modules
    payment_processor = StripePaymentProcessor()
    inventory_manager = SQLInventoryManager()
    notification_service = EmailNotificationService()

    # Create instance of high-level module, injecting dependencies
    order_processor = OrderProcessor(payment_processor, inventory_manager, notification_service)

    # Create an order
    order_items = [
        OrderItem("PROD1", 2),
        OrderItem("PROD2", 1)
    ]
    order = Order("ORD001", order_items, 100.00)

    # Process the order
    order_processor.process_order(order)
