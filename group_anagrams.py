def group_anagrams(words):
    groups = {}

    for word in words:
        key = "".join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    return list(groups.values())        

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
