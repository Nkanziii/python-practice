balance = 0 

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Quit")

    choice = input("Choose option: ")

    if choice == "1":
        add_amount = float(input("How much would you like to add? "))
        balance += add_amount
    elif choice == "2":
        withdraw_amount = float(input("How much would you like to add? "))
        if balance >= withdraw_amount:
            balance -= withdraw_amount
        else:
            print("Insufficient funds")
    elif choice == "3":
        print(f"Current balance: {balance}")
    elif choice == "4":
        break

    
