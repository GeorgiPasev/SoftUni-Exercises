import sys

whole_number_input = input()
biggest_number = -sys.maxsize

while whole_number_input != "Stop":
    whole_number_input = int(whole_number_input)
    if biggest_number < whole_number_input:
        biggest_number = whole_number_input
    whole_number_input = input()

print(biggest_number)