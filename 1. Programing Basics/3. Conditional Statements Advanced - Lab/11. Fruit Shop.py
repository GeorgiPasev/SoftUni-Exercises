fruit = input()
day_of_the_week = input()
amount = float(input())

price = 0
if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday"\
    or day_of_the_week == "Thursday" or day_of_the_week == "Friday":
    if fruit == "banana":
        price = 2.5
    elif fruit == "apple":
        price = 1.2
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.7
    elif fruit == "pineapple":
        price = 5.5
    elif fruit == "grapes":
        price = 3.85
else:
    if fruit == "banana":
        price = 2.7
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.9
    elif fruit == "grapefruit":
        price = 1.6
    elif fruit == "kiwi":
        price = 3
    elif fruit == "pineapple":
        price = 5.6
    elif fruit == "grapes":
        price = 4.2

final_price = price * amount
if not (day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday"\
    or day_of_the_week == "Thursday" or day_of_the_week == "Friday" or day_of_the_week == "Saturday"\
        or day_of_the_week == "Sunday") or not (fruit == "banana" or fruit == "apple"\
            or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or fruit == "pineapple"\
                or fruit == "grapes"):
                print("error")
else:
    print(f"{final_price:.2f}")