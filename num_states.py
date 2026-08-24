user_count = []

while True:

    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    user_count.append(float(user_input))

print(f"List of counts: {user_count}")

user_sum = sum(user_count)
print(f"Sum of counts: {user_sum}")

user_min = min(user_count)
print(f"Minimum value: {user_min}")

user_max = max(user_count)
print(f"Maximum value: {user_max}")

average = sum(user_count) / len(user_count)
print(f"Average is: {average}")

    