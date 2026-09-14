import json
import os 

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone 
        self.email = email

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"

    def to_dict(self):
        return {"Name": self.name, "Phone": self.phone, "Email": self.email}

class ContactBook:
    def __init__(self):
        self.contacts = []
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as f:
                data = json.load(f)
            self.contacts = [Contact(d["name"], d["phone"], d["email"]) for d in data]
     

    def add_contact(self, contact):
        self.contacts.append(contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return "Not found"

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return f"{name} deleted"
        return "Not found"

    def save(self):
        data = [contact.to_dict() for contact in self.contacts]
        with open("contacts.json", "w") as f:
            json.dump(data, f)

    def show_all(self):
        for contact in self.contacts:
            print(contact)
        

