def word_frequency(str):
    results = {}
    splitting = str.split()

    for char in splitting:
        if char in results:
            results[char] += 1
        else:
            results[char] = 1

    return results

print(word_frequency("the cat sat on the mat the cat"))

