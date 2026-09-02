# Sereies of function

def squares(arr):
    results = [num * num for num in arr]
    return results

#print(squares([1, 2, 3, 4, 5]))

def even_numbers(arr):
    results = [num for num in arr if num % 2 == 0]
    return results

#print(even_numbers([1, 2, 3, 4, 5, 6]))

def word_lengths(arr):
   results = {word: len(word) for word in arr}
   return results

print(word_lengths(["hello", "world", "python"]))