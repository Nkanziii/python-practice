# DAY 2
def filter_long_streaks(arr):
    result = []
    for num in arr:
        if num > 3:
            result.append(num) # the-list-im-adding-to.append(the actual thing i wanna add to the list)

    return result 

# DAY 2
def count_above(arr, num):
    counter = 0
    for n in arr:
        if n > num:
            counter += 1
        
    return counter


def find_longest(arr):
    word = ""
    for item in arr:
        if len(item) > len(word):
            word = item

    return word

# day 6

def sum_evens(arr):
    total = 0
    for item in arr:
        if item % 2 == 0:
            total += item
    
    return total

# day 7

def chunk_text(text, chunk_size):

    chunks = []
    
    words = text.split()
    
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i: i + chunk_size]))

    return chunks

# 

def clean_text(text):

    words = text.split()

    return " ".join(words)

    
# 
def group_by_source(chunks):
    grouped = {}
    for chunk in chunks:
        source = chunk["source"]

        if source not in grouped: 
            grouped[source] = []

        grouped[source].append(chunk["text"])

    return grouped

#
def count_chunks_per_source(chunks):
   count = {}

   for chunk in chunks:
       source = chunk["source"]

       if source not in count:
           count[source] = 1
       else:
           count[source] += 1
    
   return count        

#

def filter_short_answers(answers, min_length):

    filtered = []

    for answer in answers:
        if len(answer) > min_length:
            filtered.append(answer)

    return filtered

#
def reverse_string(text):
    result = ""

    for char in text:
        result = char + result

    return result

# 
def is_palindrome(text):
        
        if text[::-1] == text:
            return True
        else:
            return False

# also can write
# def is_palindrome(text):
#   return text[::-1] == text
#   

def flatten(arr):
    result = []

    for num in arr:
        for sub_num in num:
            result.append(sub_num)

    return result

# print(flatten([[1, 2], [3, 4], [5, 6]]))
        

# 
person = {
    "name": "Niki",
    "age": 24,
    "city": "London"
}

 #print(person["name"])
person["job"] = "AI Engineer"
#print(person)
#print(person.keys())

#
def count_chars(str):

    result = {}

    for item in str:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

# print(count_chars("hello"))

#

def merge_dicts(dic1, dic2):
    result = {}

    for item in dic1:
        if item in result:
            result[item] += dic1[item]
        else:
            result[item] = dic1[item]

    for char in dic2:
        if char in result:
            result[char] += dic2[char]
        else:
            result[char] = dic2[char]
    return result
       

# print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))

def invert_dict(dic):
    result = {}

    for x, y in dic.items():
        result[y] = x
    return result
        

# print(invert_dict({"a": 1, "b": 2, "c": 3}))
# returns {1: "a", 2: "b", 3: "c"})

#

def remove_duplicates(arr):
    results = []

    for item in (arr):
        if item not in results:
            results.append(item)


    return results

# print(remove_duplicates([1, 2, 3, 2, 1, 4]))

# 
def group_by_letter(arr):
    results = {}
    
    for item in arr:
        if item[0] in results:
           results[item[0]].append(item)
        else:
            results[item[0]] = [item]

            
    #return results

# print(group_by_letter(["apple", "banana", "avocado", "blueberry", "cherry"]))
# returns {"a": ["apple", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry"]}

# 

def two_sum(arr, num):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == num:
                return[i, j]

# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([3, 2, 4], 6))


#
def count_vowels(sentence):
    vowels = ["a", "e", "i", "o", "u"]

    counter = 0


    for char in sentence:
        if char in vowels:
            counter += 1

    return counter


# print(count_vowels("hello world"))

def find_duplicates(arr):
    new_list = []
    removed = []

    for num in arr:
        if num not in new_list:
            new_list.append(num)
        else:
            new_list.remove(num)
            removed.append(num)
            
    return removed

# print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
# print(find_duplicates([1, 2, 3, 4]))

def num_to_words(num):
    numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

    return numbers[num]
# print(num_to_words(2))

def title_case(str):
    results = ""

    words = str.split()

    for char in words:
        results += char[0].upper() + char[1:] + " "

    return results

    

# print(title_case("hello world"))
# print(title_case("i love python"))

def validate_password(str):
    has_digit = False
    has_upper = False
    has_length = len(str) >= 8

    for char in str:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif str == has_length:
            return True
   
    return has_digit and has_upper and has_length 


#print(validate_password("Hello1world"))
#print(validate_password("hello"))
#print(validate_password("HelloWorld"))

def most_frequent(arr):
    results = {}

    for item in arr:
        if item in results:
            results[item] += 1
        else:
            results[item] = 1
    
    return max(results, key=lambda x: results[x])
    

        
# print(most_frequent([1, 3, 2, 1, 4, 1, 3]))

def reverse_list(arr):
    results = []

    for item in range(len(arr)-1, -1, -1):
        results.append(arr[item])

        
    return results

# print(reverse_list([1, 2, 3, 4, 5]))
# print(reverse_list([10, 20, 30, 40, 50]))

# range(start, stop, step)

def is_anagram(word_one, word_two):

    return sorted(word_one) == sorted(word_two)

# print(is_anagram("listen", "silent"))
# print(is_anagram("hello", "world"))

def word_count(str):

    return len(str.split(" "))

# print(word_count("hello world how are you"))

def find_missing(arr):

    n = len(arr) + 1
    expected = n * (n + 1) / 2
    actual = sum(arr)
    return int(expected - actual)
    

#print(find_missing([1, 2, 4, 5, 6]))

def is_balanced(str):
    counter = 0

    for char in str:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1
        if counter < 0:
            return False

    return counter == 0
          

#print(is_balanced("(hello)"))     # True
#rint(is_balanced("(hello"))      # False
#print(is_balanced("((hello))"))   # True
#print(is_balanced(")("))          # False)
    
def is_anagram(str1, str2):
    word = str1.replace(" ", "").lower()
    word_two = str2.replace(" ", "").lower()

    return sorted(word) == sorted(word_two)

    

#print(is_anagram("Listen", "Silent"))
#print(is_anagram("Astronomer", "Moon starer"))
#print(is_anagram("hello", "world"))

def count_upper(str):
    results = 0

    for char in str:
        if char.isupper():
            results += 1
    return results

#print(count_upper("Hello World"))
#print(count_upper("PYTHON"))
#print(count_upper("hello"))

def sum_digits(num):
    string = str(num)

    results = []

    for char in string:
        number = int(char)
        results.append(number)
    return sum(results)
        

#print(sum_digits(123))

def remove_vowels(str):
    vowels = ["a", "e", "i", "o", "u"]

    results = []

    for char in str:
        if char not in vowels:
            results.append(char)

    return "".join(results)


#print(remove_vowels("hello world"))
def common_elements(arr1, arr2):
    results = []

    for item in arr1:
        for char in arr2:
            if item == char:
                results.append(item)

    return results

#print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
#print(common_elements(["apple", "banana"], ["banana", "cherry"]))

# Also can do:
# for item in arr1:
#   if item in arr2:
#       results.append(item)

def flatten(arr):
    results = []

    for item in arr:
        if isinstance(item, list):
            results.extend(flatten(item))
        else:
            results.append(item)

    return results

#print(flatten([1, [2, 3], [4, [5, 6]], 7]))

def squares(arr):
    results = [num * num for num in arr]
    return results

print(squares([1, 2, 3, 4, 5]))

