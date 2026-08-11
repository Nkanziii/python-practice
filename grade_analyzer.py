students = {}

while True:

    name = input("Enter name: ")

    if name == "done" : break

    grade = input("Enter grade: ")

    students[name] = float(grade)



highest = max(students.values())
lowest = min(students.values())
average = round(sum(students.values()) / len(students), 2)

for name, grade in students.items():
    print(f"{name}: {grade}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {average}")



