def caesar_cipher(str, num):
    result = ""
    for char in str:
        within_alpha = ord(char) - ord('a')
        shifted = (within_alpha + num) % 26 
        result += chr(shifted + ord('a'))
    return result


print(caesar_cipher("hello", 3))
print(caesar_cipher("xyz", 2))
