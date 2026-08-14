shopping_menu = {}

while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Get total")
    print("5. Quit")

    choice = input("choose which option: ")

    if choice == "1":
        item = input("what is the item name? ")
        price = float(input("what is the price? "))
        shopping_menu[item] = price
    elif choice == "2":
        item = input("what is the item name? ")
        if item in shopping_menu:
            del shopping_menu[item]
        else:
            print("Not found")
    elif choice == "3":
        for item, price in shopping_menu.items():
            print(f"{item}: £{price}")
    elif choice == "4":
            total = sum(shopping_menu.values())
            print(f"Total: £{total}")
    elif choice == "5":
        break 
