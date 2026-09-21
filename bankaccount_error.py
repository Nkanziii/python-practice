class InsufficientFundsError(Exception): #convention to end with error
    pass

class NegativeAmountError(Exception):
    pass

class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def withdraw(self, amount: float):
        if amount < 0:
            raise NegativeAmountError("Amount cannot be negative")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds")
        self.balance -= amount

    def __str__(self) -> str:
        return f"Balance: {self.balance}"

account = BankAccount(100)
print(account)

try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)

try:
    account.withdraw(-50)
except NegativeAmountError as e:
    print(e)