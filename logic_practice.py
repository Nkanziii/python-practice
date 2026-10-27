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

def is_palindrome(str):
    cleaned = str.replace(" ","").lower()

    return cleaned == cleaned[::-1]
        

print(is_palindrome("niki "))
print(is_palindrome("A man a plan a canal Panama"))
    
def count_vc(str):
    results = {"vowels": 0, "consonants": 0}
    vowels = ["a", "e", "i", "o", "u"]
    cleaned = str.replace(" ", "").strip().lower()

    for char in cleaned:
        if char in vowels:
            results["vowels"] += 1
        else:
            results["consonants"] += 1
            

    return results

print(count_vc("Hello World"))

def remove_nums(arr):
    numbers = [1,2,3,4,5]

    for num in numbers:
        if num % 2 == 0:
            numbers.remove(num)

    return numbers

print(remove_nums([1, 2, 3, 4, 5]))

def remove_sorted_duplicates(arr):

    results = []
    prev = None

    for num in arr:
        if num != prev:
            results.append(num)

        prev = num

    return results

print(remove_sorted_duplicates([1, 1, 2, 3, 3, 4]))

def merge_sorted(list1, list2):
    results = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            results.append(list1[i])
            i += 1
        else:
            results.append(list2[j])
            j += 1

    results += list1[i:]
    results += list2[j:]

    return results

print(merge_sorted([1, 3, 5], [2, 4, 6]))
print(merge_sorted([1, 2, 3], [4, 5, 6]))


def max_subarray(arr):
    current_sum = 0
    max_sum = 0

    for num in arr:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)

    return max_sum


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

def find_duplicate(arr):
    results = {}

    for num in arr:
        if num in results:
            results[num] += 1
        else:
            results[num] = 1

    for x, y in results.items():
        if y == 2:
            return x

print(find_duplicate([1, 3, 4, 2, 2]))
print(find_duplicate([3, 1, 3, 4, 2]))


def max_window_sum(arr, k):

    max_window = 0

    for i in range(len(arr) - k + 1):
        window = arr[i:i+k]
        window_sum = sum(window)
        max_window = max(max_window, window_sum)

    return max_window

    

print(max_window_sum([2, 1, 5, 1, 3, 2], 3))
print(max_window_sum([1, 4, 2, 9, 7, 3], 2))