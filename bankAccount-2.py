import json
import os

class BankAccount:
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

    def to_dict(self):
        results = {"owner": self.owner, "balance": self.balance}
        return results

def save_accounts( accounts):
    data = [account.to_dict() for account in accounts]
    with open("accounts.json", "w") as f:
        json.dump(data, f)

def load_accounts():
    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as f:
            data = json.load(f)
        return [BankAccount(d["owner"], d["balance"]) for d in data]
    return []
    
accounts = load_accounts()

while True:
    print("1. Add acoount")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5 . Save and quit")

    choice = input("Pick and option: ")

    if choice == "1":
        owner = input("Owner name: ")
        balance = float(input("Starting balance: "))
        accounts.append(BankAccount(owner, balance))
    elif choice == "2": 
        owner = input("Account owner: ")
        amount = float(input("Amount: "))
        for account in accounts:
            if account.owner == owner:
                account.deposit(amount)
    elif choice == "3":
        owner = input("Account owner: ")
        amount = float(input("Amount: "))
        for account in accounts: 
            if account.owner == owner:
                account.withdraw(amount)
    elif choice == "4":
        owner = input("Account owner: ")
        for account in accounts:
            if account.owner == owner:
                print(account.get_balance())
    elif choice == "5":
        save_accounts(accounts)
        break