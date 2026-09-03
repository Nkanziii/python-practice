def safe_divide(num, num2):
    try:
        result = num / num2
        return int(result)
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(safe_divide(10, 2))
print(safe_divide(10, 0))


