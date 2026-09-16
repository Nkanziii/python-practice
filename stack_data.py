class Stack:
    def __init__(self):
        self.items = []

    def push(self, item): # pushes to list
        self.items.append(item)

    def pop(self): # removes the last item
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1] # returns the last item with out removing it

    def is_empty(self): # checks if a list is empty
        return not bool(self.items)    

    def __len__(self): # length of the list
        return len(self.items)

    def __str__(self): 
        return f"Stack contents: {self.items}"      


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())
print(len(s))
print(s)