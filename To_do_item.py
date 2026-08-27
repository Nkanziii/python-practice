class ToDoItem:
    def __init__(self, task, done=False):
        self.task = task
        self.done = done

    def complete(self):
        self.done=True

    
    def __str__(self):
        if self.done:
            return f"✓ {self.task}"
        else:
            return f"✗ {self.task}"

item = ToDoItem("Buy groceries")
print(item)
item.complete()
print(item)       
