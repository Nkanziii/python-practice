filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        lines = content.split("/n")
        words = content.split()
        characters = len(content)
        longest = max(content.split("\n"), key=lambda x: len(x))
except FileNotFoundError:
    print("File not found")


print(f"Total lines: {len(lines)}")
print(f"Total words: {len(words)}")
print(f"Total characters: {characters}")
print(f"Longest line: {longest}")