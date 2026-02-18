n = int(input())

for number in range(1111, 10000):
    special_number = True
    # if "0" in number_as_string: (instead of the if down in the loop)
    # continue 
    for digit in str(number):
        digit = int(digit)
        if digit == 0 or n % digit != 0:
            special_number = False
            break
    if special_number:
        print(number, end=" ")
    