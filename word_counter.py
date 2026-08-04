user_input = input("Type a sentence")

split_words = user_input.split()
count = {}

for word in split_words:
    if word in count:
        count[word] += 1
    else :
        count[word] = 1

for word in count:
    print(word, count[word])


