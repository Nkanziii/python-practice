def find_pairs(arr, target):
    pairs = []

    for item1 in range(len(arr)):
        for item2 in range(item1+1, len(arr)):
            if arr[item1] + arr[item2] == target:
                pairs.append((arr[item1], arr[item2]))

    if not pairs:
        print("No pairs found")
    return pairs
            

print(f"Answer to the first problem: {find_pairs([1, 2, 3, 4, 5], 6)}")


def longest_consecutive(arr):
    sorted_arr = sorted(arr)
    current_counter = 0
    longest = 0
    prev = sorted_arr[0]

    for num in sorted_arr[1:]:
        if num - prev == 1:
            current_counter += 1
            longest = max(longest, current_counter)
        else:
            current_counter = 1
        
        prev = num

    return longest

print(f"Answer to the second problem: {longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])}")


def rotate_list(arr, k):
    results = []

    for num in arr:
        rotated = arr[-k:] + arr[:-k]
        results.append(rotated)

    return rotated

    #loop is unnecessary could have just done:
    # return arr[-k:] + arr[:-k]

print(f"Answer to the third problem: {rotate_list([1, 2, 3, 4, 5], 2)}")


def valid_paranthese(str):
    matching = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in str:
        if char in matching:
            if not stack or stack.pop() != matching[char]:
                return False    
        else:
            stack.append(char)

    return len(stack) == 0

print(valid_paranthese('(())'))
print(valid_paranthese("()[]{}"))  # True
print(valid_paranthese("(]"))      # False
print(valid_paranthese("([)]"))    # False)