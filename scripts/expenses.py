expenses = []

while True:
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total")
    print("4. View by category")
    print("5. Quit")

    choice = input("Pick an option? ")

    if choice == "1":
        name = input("Item name: ")
        cost = float(input("Item cost: "))
        category = input("Item category: ")
        expenses.append({
            "name": name,
            "amount": cost,
            "category": category
        })
    elif choice == "2":
        for expense in expenses:
            print(f"{expense['name']} - £{expense['amount']} ({expense['category']})")
    elif choice == "3":
        sum_of = sum(expense["amount"] for expense in expenses)
        print(f"Total amount is: {sum_of}")
    elif choice == "4":
        which_category = input("What is the category? ")
        for expense in expenses:
            if which_category == expense["category"]:
                print(f"{expense['name']} - £{expense['amount']} ({expense['category']})")
    elif choice =="5":
        break
