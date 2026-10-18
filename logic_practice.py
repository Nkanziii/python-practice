def two_sum(arr, target):
    results = []

    for item1 in range(len(arr)):
        for item2 in range(item1+1, len(arr)):
            if arr[item1] + arr[item2] == target:
                results.append([item1, item2])

    if not results:
        print("no results")
    return results

print(two_sum([2, 7, 11, 15], 9))

def missing_number(arr):

    n = len(arr) + 1
    expected_sum = n * (n + 1) / 2
    actual_sum = sum(arr)
    missing_num = expected_sum - actual_sum

    return int(missing_num)

print(missing_number([1, 2, 4, 5, 6]))

def first_unique(str):
    counts = {}

    for char in str:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for char in str:
        if counts[char] == 1:
            return char
   
    return None

print(first_unique("aabbcde"))
    