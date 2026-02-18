command = input()
sum_simple_nums = 0
sum_composite_nums = 0

while command != "stop":
    command = int(command)
    if command < 0:
        print("Number is negative.")
    else:
        number_is_prime = True
        for number in range(2, command):
            if command % number == 0:
                number_is_prime = False
                break
        if number_is_prime:
            sum_simple_nums += command
        else:
            sum_composite_nums += command
    command = input()

print(f"Sum of all prime numbers is: {sum_simple_nums}")
print(f"Sum of all non prime numbers is: {sum_composite_nums}")