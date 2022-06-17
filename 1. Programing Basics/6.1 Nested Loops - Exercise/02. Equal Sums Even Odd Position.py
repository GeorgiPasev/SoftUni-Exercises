first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    number = str(number)
    sum_odd = 0
    sum_even = 0
    for index, character in enumerate(number):
        if index % 2 == 0: #check if even but store in odd since we start counting from 0
            sum_odd += int(character)
        else:
            sum_even += int(character)
    if sum_even == sum_odd:
        print(number, end=" ")
 