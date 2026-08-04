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

            
    return results

print(group_by_letter(["apple", "banana", "avocado", "blueberry", "cherry"]))
# returns {"a": ["apple", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry"]}