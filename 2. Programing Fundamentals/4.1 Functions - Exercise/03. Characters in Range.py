def chars_between(a, b):
    string = ''
    for char in range(ord(a) + 1, ord(b)):
        string += chr(char) + " "
    return string

first_char = input()
second_char = input()

print(chars_between(first_char, second_char))

# list (might be better if you need to delete the last interval)
def chars_between(a, b):
    collected_characters = []
    for char in range(ord(a) + 1, ord(b)):
        collected_characters.append(chr(char))
    return collected_characters


first_char = input()
second_char = input()
result = chars_between(first_char, second_char)
print(' '.join(result))