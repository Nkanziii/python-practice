from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True

p1 = Product("make-up", 24.99, True)
p2 = Product("shower-gel", 7.99, False)

print(p1.name)
print(p2.in_stock)
print(p1)
print(p2)
