number_of_strings = int(input())
banned = [',', '.', '_']

for string in range(number_of_strings):
    current_string = input()
    is_pure = True
    for char in range(len(current_string)):
        if current_string[char] in banned:
            is_pure = False
            break
    if is_pure:
        print(f"{current_string} is pure.")
    else:
        print(f"{current_string} is not pure!")
    

#Alternative
banned = [',','_','.']
lines_count = int(input())

for _ in range(lines_count):
    current_string = input()
    is_pure = True
    for letter in banned:
        if letter in current_string:
            print(f"{current_string} is not pure!")
            is_pure = False
            break
    if is_pure:
        print(f"{current_string} is pure.")

# Alternative
number_of_strings = int(input())

for string in range(number_of_strings):
    current_string = input()
    if ',' in current_string or '.' in current_string or '_' in current_string:
        print(f"{current_string} is not pure!")
          # can put here continue instead of the else
    else:
        print(f"{current_string} is pure.")

