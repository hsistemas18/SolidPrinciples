from abc import ABC, abstractmethod

# Smaller, more focused interfaces
class OrderProcessor(ABC):
    @abstractmethod
    def process(self, order):
        pass

class PaymentProcessor(ABC):
    @abstractmethod
    def charge(self, order):
        pass

class ShippingProcessor(ABC):
    @abstractmethod
    def ship(self, order):
        pass

class InventoryManager(ABC):
    @abstractmethod
    def update_inventory(self, order):
        pass

# Concrete implementations
class StandardOrderProcessor(OrderProcessor, PaymentProcessor, ShippingProcessor, InventoryManager):
    def process(self, order):
        print(f"Processing standard order {order.id}")

    def charge(self, order):
        print(f"Charging ${order.total} for order {order.id}")

    def ship(self, order):
        print(f"Shipping order {order.id} to {order.address}")

    def update_inventory(self, order):
        print(f"Updating inventory for order {order.id}")

class DigitalOrderProcessor(OrderProcessor, PaymentProcessor, InventoryManager):
    def process(self, order):
        print(f"Processing digital order {order.id}")

    def charge(self, order):
        print(f"Charging ${order.total} for digital order {order.id}")

    def update_inventory(self, order):
        print(f"Updating digital inventory for order {order.id}")

class InStorePickupProcessor(OrderProcessor, PaymentProcessor, InventoryManager):
    def process(self, order):
        print(f"Processing in-store pickup order {order.id}")

    def charge(self, order):
        print(f"Charging ${order.total} for in-store pickup order {order.id}")

    def update_inventory(self, order):
        print(f"Updating inventory for in-store pickup order {order.id}")

# Order class
class Order:
    def __init__(self, id, total, address=None):
        self.id = id
        self.total = total
        self.address = address

# Client code
def process_order(processor: OrderProcessor, order: Order):
    processor.process(order)
    
    if isinstance(processor, PaymentProcessor):
        processor.charge(order)
    
    if isinstance(processor, ShippingProcessor):
        processor.ship(order)
    
    if isinstance(processor, InventoryManager):
        processor.update_inventory(order)

# Usage
if __name__ == "__main__":
    standard_order = Order("SO001", 100, "123 Main St")
    digital_order = Order("DO001", 50)
    pickup_order = Order("PO001", 75)

    standard_processor = StandardOrderProcessor()
    digital_processor = DigitalOrderProcessor()
    pickup_processor = InStorePickupProcessor()

    print("Processing Standard Order:")
    process_order(standard_processor, standard_order)
    print("\nProcessing Digital Order:")
    process_order(digital_processor, digital_order)
    print("\nProcessing In-Store Pickup Order:")
    process_order(pickup_processor, pickup_order)
