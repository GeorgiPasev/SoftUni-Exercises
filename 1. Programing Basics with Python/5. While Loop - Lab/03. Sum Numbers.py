whole_number = int(input())
sum_of_numbers = int(input())

while not sum_of_numbers >= whole_number:
    new_number = int(input())
    sum_of_numbers += new_number

print(sum_of_numbers)