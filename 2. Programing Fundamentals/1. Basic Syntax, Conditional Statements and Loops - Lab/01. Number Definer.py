floating_number = float(input())

if floating_number == 0:
    print("zero")
elif 0 < floating_number: # positive number
    if floating_number < 1:
        print("small", end = " ")
    elif floating_number > 1000000:
        print("large", end = " ")
    print("positive")
else: # negative number
    if abs(floating_number) < 1:
        print("small", end = " ")
    elif abs(floating_number) > 1000000:
        print("large", end = " ")
    print("negative")
