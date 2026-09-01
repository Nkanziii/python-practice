class Products:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Name: {self.name} - {self.quantity} qty in stock - £{self.price} each"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def restock(self, name, amount):
        for product in self.products:
            if product.name == name:
                product.quantity += amount

    def sell(self, name, amount):
        for product in self.products:
            if product.name == name:
                if product.quantity < amount:
                    print("Not enough stock")
                else:
                    product.quantity -= amount

    def show_all(self):
        for product in self.products:
            print(product)

    def total_value(self):
        return sum(p.quantity * p.price for p in self.products)

inv = Inventory()
inv.add_product(Products("Apple", 100, 0.50))
inv.add_product(Products("Banana", 50, 0.30))
inv.add_product(Products("Orange", 75, 0.80))

inv.show_all()
print(f"Total balue: £{inv.total_value()}")
inv.sell("Apple", 20)
inv.restock("Banana", 30)
inv.show_all()
