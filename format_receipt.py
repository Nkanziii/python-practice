def format_receipt(items):
    print("-" * 20)
    for item, price in items:
        print(f"{item:<15} £{price:.2f}")
    print("-" * 20)
    total = sum(price for item, price in items)
    print(f"{'Total:':<15} £{total:.2f}")

items = [("Coffee", 3.50), ("Sandwich", 6.99), ("Water", 1.50)]
print(format_receipt(items))
