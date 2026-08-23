inventory = {}

while True:
    print("1. Add stock")
    print("2. Remove stock")
    print("3. View inventory")
    print("4. Check if item exists")
    print("5. Quit")

    choice = input("Pick an option: ")

    if choice == "1":
        item = input("What item would you like to add: ")
        quantity = float(input("How many would you like to add: "))
        inventory[item] = quantity
    elif choice == "2":
        item_remove = input("what item do you want to remove: ")
        quantity_remove = float(input("How much would you like to remove: "))
        if inventory[item_remove] >= quantity_remove:
            inventory[item_remove] -= quantity_remove
            if inventory[item_remove] == 0:
                del inventory[item_remove]
        else:
            print("Not enough stock")
    elif choice == "3":
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    elif choice == "4":
        item_name = input("what item would you like to check: ")
        if item_name in inventory:
            print(f"{item_name}: {inventory[item_name]}")
        else:
            print("Not found")
    elif choice == "5":
        break

        

