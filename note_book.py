from datetime import date
import json
import os

class Note:
    def __init__(self, title, content):
        self.title = title
        self. content = content 
        self.created_at = str(date.today())

    def __str__(self):
        return f"{self.title} ({self.created_at}): {self.content}"

    def to_dict(self):
        return {"title": self.title, "content": self.content, "date": self.created_at}

class NoteBook:
    def __init__(self):
        self.notes = []
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as f:
                data = json.load(f)
            self.notes = [Note(d["title"], d["content"]) for d in data]

    def add_note(self, note):
        self.notes.append(note)

    def search(self, keyword):
        for note in self.notes:
            if keyword in note.title or keyword in note.content:
                print(note)

    def show_all(self):
        for note in self.notes:
            print(note)

    def save(self):
        data = [note.to_dict() for note in self.notes]
        with open("notes.json", "w") as f:
            json.dump(data, f)

book_note = NoteBook()

while True:
    print("1. Add Note")
    print("2. Search for note")
    print("3. Show all notes")
    print("4. Save and exit")

    choice = input("Pick an option: ")

    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        book_note.add_note(Note(title, content))
    elif choice == "2":
        title = input("Enter note title: ")
        book_note.search(title)
    elif choice == "3":
        book_note.show_all()
    elif choice == "4":
        book_note.save()
        break

