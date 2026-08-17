counts = {}

sentence = "I love me. I want Money. I am ai engineer."

word_count = len(sentence.split(" "))
print(word_count)

total_sentence_count = total_sentence_count = len([s for s in sentence.split(".") if s.strip()])
print(total_sentence_count)

clean = sentence.replace(".", "").replace("?", "").replace("!", "").lower()

for word in clean.split():
    if word in counts:
        counts[word] += 1
    else: 
        counts[word] = 1

most_common = max(counts, key=lambda x: counts[x])

longest_word = max(clean.split(), key=lambda x: len(x))

average = round(word_count / total_sentence_count, 2)
    
print(f"Total words: {word_count}")
print(f"Total sentences: {total_sentence_count}")
print(f"Most common word: {most_common}")
print(f"Longest word: {longest_word}")
print(f"Average words per sentence: {average}")



