class bankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

niki = bankAccount("niki", 100)
niki.deposit(150)
niki.withdraw(30)

sam = bankAccount("sam", 50)
sam.deposit(200)
sam.withdraw(60)


print(f"Niki's Account: {niki.get_balance()}")
print(f"Sam's Account: {sam.get_balance()}")