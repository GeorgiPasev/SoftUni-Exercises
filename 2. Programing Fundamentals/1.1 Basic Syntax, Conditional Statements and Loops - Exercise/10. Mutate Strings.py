string_1 = input()
string_2 = input()
last_string = string_1

for symbol_index in range(len(string_2)):
    left_part = string_2[:symbol_index + 1]
    right_part = string_1[symbol_index + 1:]
    current_string = left_part + right_part
    if current_string == last_string:
        continue # removes multiples of the same word
    print(current_string)
    last_string = current_string