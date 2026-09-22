from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    available: bool = True

class BookNotFoundError(Exception):
    pass

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title: str):
        for item in self.books:
            if item.title == title:
                print(item)
                return
        raise BookNotFoundError(f"{title} not found")

    def remove_book(self, title: str):
        for item in self.books:
            if item.title == title:
                self.books.remove(item)
                return
        raise BookNotFoundError(f"{title} not found")


lib = Library()
lib.add_book(Book("Python 101", "Alice"))
lib.add_book(Book("Clean Code", "Bob"))

lib.find_book("Python 101")

try:
    lib.find_book("Missing Book")
except BookNotFoundError as e:
    print(e)

lib.remove_book("Clean Code")
lib.find_book("Python 101")