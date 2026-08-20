recipes = {}

while True:
    print("1. Add recipe")
    print("2. View recipe")
    print("3. Add ingredient to recipe")
    print("4. Delete recipe")
    print("5. Quit")

    choice = input("pick an option: ")

    if choice == "1":
        name = input("what is the name: ")
        recipes[name] = []
    elif choice == "2":
        recipe_name = input("whats the name to check: ")
        if recipe_name in recipes:
            for item in recipes[recipe_name]:
                print(item)
        else:
                print("Recipe not found")
    elif choice == "3":
        recipe_name = input("whats recipe name: ")
        ingredient = input("whats the ingredient: ")
        if recipe_name in recipes:
            recipes[recipe_name].append(ingredient)
        else: 
            print("Recipe not found")
    elif choice == "4":
        remove = input("what do u wanna delete: ")
        del recipes[remove]
    elif choice == "5":
        break
