tasks = {}

while True:
    print("1. Add task")
    print("2. Complete task")
    print("3. View tasks")
    print("4. Quit")

    choice = input("Pick an option: ")

    if choice == "1":
        add_task = input("Add task: ")
        tasks[add_task] = False           
    elif choice == "2":
        task_name = input("Which task: ")
        if task_name in tasks:
            tasks[task_name] = True
        else:
            print("Task not found")
    elif choice == "3":
        for x, y in tasks.items():
            status = "✓" if y == True else "x"
            print(f"{x}: {status}")
    elif choice == "4":
        break

        
