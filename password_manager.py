passwords = {}

while True :
    print("1. Add password")
    print("2. Get password")
    print("3. List all sites")
    print("4. Quit")

    choice = input("Pick an option: ")

    if choice == "1":
        site =input("Enter site: ")
        user_password = input("Enter passowrd: ")
        result = ""
        for char in user_password:
            within_alpha = ord(char) - ord('a')
            shifted = (within_alpha + 13) % 26 
            result += chr(shifted + ord('a'))
        passwords[site] = result

    elif choice == "2":
        site = input("Which site: ")
        result = ""
        for x, y in passwords.items():
            if x == site:
                for char in y:
                    within_alpha = ord(char) - ord('a')
                    unshifted = (within_alpha - 13) % 26
                    result += chr(unshifted + ord('a'))
                print(result)

    elif choice == "3":
        for x, y in passwords.items():
            print(f"Sites : {x}")

    elif choice == "4":
        break

            
