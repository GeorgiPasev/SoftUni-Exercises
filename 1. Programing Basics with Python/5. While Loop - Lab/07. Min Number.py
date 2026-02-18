import sys

whole_number_input = input()
smallest_number = sys.maxsize

while whole_number_input != "Stop":
    whole_number_input = int(whole_number_input)
    if smallest_number > whole_number_input:
        smallest_number = whole_number_input
    whole_number_input = input()

print(smallest_number)