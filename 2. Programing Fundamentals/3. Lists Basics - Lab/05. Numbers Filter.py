n = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'
numbers = []
filtered_numbers = []

for _ in range(n):
    current_number = int(input())
    numbers.append(current_number)
#numbers = [int(input()) for _ in range(n)] #alternative for loop

command = input()

for num in numbers:
    filter_command = (
        (command == COMMAND_EVEN and num % 2 == 0) or 
        (command == COMMAND_ODD and num % 2 != 0) or 
        (command == COMMAND_POSITIVE and num >= 0) or 
        (command == COMMAND_NEGATIVE and num < 0)
    )

    if filter_command:
        filtered_numbers.append(num)

print(filtered_numbers)
