def clean_text(str):
    stripped = str.strip()
    lower_case = stripped.lower()
    replaced = lower_case.replace("  ", " ")
    return replaced



#print(clean_text(" Hello World "))

def invert_and_filter(dic):
    results = {}

    for x, y in dic.items():
        if y > 10:
            results[y] = x

    return results

print(invert_and_filter({"a": 5, "b": 15, "c": 20, "d": 3}))
