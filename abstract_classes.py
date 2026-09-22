from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof"

    def move(self):
        return "crawl"

class Bird(Animal):
    def speak(self):
        return "tweet"

    def move(self):
        return "fly"

class Lion(Animal):
    def speak(self):
        return "rawer"
    def move(self):
        return "pounce"

    

d = Dog()
b = Bird()
l = Lion()

print(d.speak())
print(b.move())
print(l.move())
