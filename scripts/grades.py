students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "Diana": 60,
    "Eve": 78
}

names = students.keys()
grades = students.values()


for x, y in students.items():
    
    if y > 90:
        print(f"{x}: {y} - A")
    elif y >= 80 and y <= 89:
        print(f"{x}: {y} - B")
    elif y >= 70 and y <= 79:
        print(f"{x}: {y} - C")
    elif y >= 60 and y <= 69:
        print(f"{x}: {y} - D")
    else:
        print(f"{x}: {y} - F")


class_average = sum(grades)/len(grades)


print(f"Class average is: {class_average}")
