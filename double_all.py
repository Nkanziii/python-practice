def double_all(num):
    return num * 2

print(list(map(double_all, [1, 2, 4])))

def keep_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(list(filter(keep_even, [1, 2, 5, 8, 6])))

def keep_positive(num):
    if num > 0:
        return True
    else:
        return False

    # or can write the if else statement as one like return num > 0 for simplified version

print(list(filter(keep_positive, [-2, -3, -5, 1, 0, 4])))
