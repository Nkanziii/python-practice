class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, subject, score):
        self.grades.append({"subject": subject, "score": score})

    def average_grade(self):
        scores = [g["score"] for g in self.grades]
        return sum(scores) / len(scores)
    
    def __str__(self):
       return f"{self.name} ({self.age}) - Average: {self.average_grade()}"

students = [
    Student("Alice", 20),
    Student("Bob", 22),
    Student("Charlie", 19)
]

students[0].add_grade("math", 85)
students[0].add_grade("english", 90)

students[1].add_grade("computer-science", 70)
students[1].add_grade("biology", 81)

students[2].add_grade("history", 69)
students[2].add_grade("physics", 81)


high_achievers = [s for s in students if s.average_grade() > 80]
print("High achievers: ")
for s in high_achievers:
    print(s)