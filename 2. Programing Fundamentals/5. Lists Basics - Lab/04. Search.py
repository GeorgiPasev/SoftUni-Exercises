number_of_strings = int(input())
filter_word = input()
my_list = []

for _ in range(number_of_strings):
    current_string = input()
    my_list.append(current_string)

print(my_list)
filtered_list = my_list

for string in range(len(my_list) - 1, -1, -1):
    element = my_list[string]
    if filter_word not in element:
        my_list.remove(element)
print(my_list)