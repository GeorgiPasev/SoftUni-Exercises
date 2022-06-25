def bring_min(some_numbers):
    return min(some_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())

all_numbers = [first_number, second_number, third_number]
min_number = bring_min(all_numbers)

print(min_number)