class Task:
    def __init__(self, title, priority, done=False):
        self.title = title
        self.priority = priority
        self.done = done


    def complete(self):
        self.done=True

    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.title} (Priority: {self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()

    def show_by_priority(self):
        return sorted(self.tasks, key=lambda x: x.priority)

    def show_pending(self):
        for task in self.tasks:
            if not task.done:
                print(f"Incomplete tasks: {task}")

    def __len__(self):
        return len(self.tasks)

    def __contains__(self, title):
        return any(task.title == title for task in self.tasks)

tm = TaskManager()
tm.add_task(Task("Buy groceries", 2))
tm.add_task(Task("Fix bug", 1))
tm.add_task(Task("Call mum", 3))

tm.complete_task("Buy groceries")

print("--- By Priority ---")
for task in tm.show_by_priority():
    print(task)

print("--- Pending ---")
tm.show_pending()

print(len(tm))

print("Fix bug" in tm)