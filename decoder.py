message = input("Write word: ")

shift_number = int(input("Enter shift number: "))

result = ""

for char in message:
    if char.isalpha():
        character = ord(char.lower()) - ord('a')
        shift = (character - shift_number) % 26
        result += chr(shift + ord('a'))
    else:
        result += char
        
print(result)