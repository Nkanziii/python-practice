def move_zeros(arr):
    results = []
    
    for num in arr:
        if num != 0:
            results.append(num)
            
    dif_zeros = len(arr) - len(results) 
    
    return results + [0] * dif_zeros

    
print(f"The answer to the 1st problem is: {move_zeros([0, 4, 6, 0, 8])}")
print(f"The answer to the 2nd problem is: {move_zeros([1, 2, 3])}")
print(f"The answer to the 3rd problem is: {move_zeros([])}")


def has_duplicates(arr):
    results = {}
    
    for char in arr:
        if char in results:
            results[char] += 1
        else:
            results[char] = 1
            
    for x, y in results.items():
        if y > 1:
            return True
            
    return False
            
print(f"The answer to the 4th problem is: {has_duplicates([1, 2, 2, 2 , 3 , 4])}")
print(f"The answer to the 5th problem is: {has_duplicates([1, 2, 3])}")
print(f"The answer to the 6th problem is: {has_duplicates([])}")

def duplicates(arr):
    set_list = set(arr)
    
    return len(arr) > len(set_list)
    
print(f"The answer to the 6th problem is: {duplicates([1, 2, 2, 2 , 3 , 4])}")
print(f"The answer to the 7th problem is: {duplicates([1, 2, 3])}")
