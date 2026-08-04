with open("sample.txt", "w") as f:
    f.write("i love me. i am grateful. i am rich")

with open("sample.txt", "r") as f:
        text = f.read()

words = text.split()

total_words = len(words)

count = {}

for item in words:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1


sorted_words = sorted(count.items(), key=lambda x: x[1], reverse=True)

print(f"Total words are: {total_words}")

print("Top 3 most common words:")
for word, count in sorted_words[:3]:
     print(f"{word}: {count}")


      



