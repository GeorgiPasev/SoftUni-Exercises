list_of_numbers = input().split()
for element in list_of_numbers:
    opposite_number = int(element) * -1
    index = list_of_numbers.index(element)
    list_of_numbers[index] = opposite_number
print(list_of_numbers)

#Alternative
list_of_numbers = input().split()
for index, element in enumerate(list_of_numbers):
    opposite_number = -int(element)
    list_of_numbers[index] = opposite_number
print(list_of_numbers)


# Alternative
list_of_numbers = input().split()
opposite_numbers = []
for element in list_of_numbers:
    opposite_numbers.append(-int(element))
print(opposite_numbers)