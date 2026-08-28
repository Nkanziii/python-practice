class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
        

    def __str__(self):
        status = "available" if self.available else "borrowed"
        return f"{self.title} by {self.author} ({status})"
        

class Library:
    def __init__(self):
        self.book = []

    def add_book(self, book):
        self.book.append(book)

    def borrow_book(self, title):
        for book in self.book:
            if book.title == title:
                book.available=False

    def return_book(self, title):
        for book in self.book:
            if book.title == title:
                book.available=True

    def show_available(self):
        for book in self.book:
            if book.available:
                print(book)

lib = Library()
lib.add_book(Book("Python 101", "Alice"))
lib.add_book(Book("Clean Code", "Bob"))
lib.borrow_book("Python 101")
lib.show_available()