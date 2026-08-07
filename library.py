books = {}

while True:
    print("1. Add book")
    print("2. Borrow book")
    print("3. Return book")
    print("4. View available books")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        book_name = input("What is the name of the book? ")
        books[book_name] = True
    elif choice == "2":
        book_name = input("What is the name of the book? ")
        if book_name in books and books[book_name] == True:
            books[book_name] = False
        else:
            print("Book not available")
    elif choice == "3":
        book_name = input("What is the name of the book? ")
        books[book_name] = True
    elif choice == "4":
        for book_name, available in books.items():
            if available == True:
                print(book_name)
    elif choice == "5":
        break

