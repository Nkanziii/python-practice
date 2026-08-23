import json
import os

if os.path.exists("grades.json"):
    with open("grades.json", "r") as f:
        students = json.load(f)
else:
    students = {}

while True:
    print("1. Add studnet")
    print("2. View all students")
    print("3. Get average grade")
    print("4. save and quite")

    choice = input("choose an option: ")

    if choice == "1":
        name = input("Name of the student: ")
        grade = float(input("whats the grade: "))
        students[name] = grade
    elif choice == "2":
        for x, y in students.items():
            print(f"{x}: {y}")
    elif choice == "3":
        average = round(sum(students.values()) / len(students), 2) 
        print(average)
    elif choice == "4":
        with open("grades.json", "w") as f:
            json.dump(students, f)
            break