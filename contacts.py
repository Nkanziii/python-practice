contact = {}

while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Show all")
    print("4. Quit")

    choice = input("Pick an option: ")

    if choice == "1":
        contact_name = input("What is contact name? ")
        contact_num = input("what is contact number? ")
        contact[contact_name] = contact_num
    elif choice == "2":
        contact_name = input("what is contact name? ")
        if contact_name in contact:
            print(contact[contact_name])
        else:
            print("Not found")
    elif choice == "3":
        for name, number in contact.items():
            print(f"{name}: {number}")
    elif choice == "4":
        break


