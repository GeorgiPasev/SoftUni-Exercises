vowels = ['a', 'o', 'u', 'e', 'i']

text = [letter for letter in input() if letter.lower() not in vowels]


print("".join(text))