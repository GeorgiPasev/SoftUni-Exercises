letters = input()

for letter in sorted(set(letters)):
    times = letters.count(letter)
    print(f"{letter}: {times} time/s")

#alt
text = input()

[print(f"{symbol}: {text.count(symbol)} time/s") for symbol in sorted(set(text))]

#alt
chars = input()
my_dict = {}

for char in chars:
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1

for key in sorted(my_dict):
    print(f"{key}: {my_dict[key]} time/s")