def second_largest(arr):

    largest = 0
    second = 0

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num

    return second 

print(second_largest([3, 1, 4, 1, 5, 9, 2, 6]))  # should be 6
print(second_largest([1, 9, 2]))                   # should be 2
print(second_largest([5, 9, 1]))                   # should be 5
