hour = int(input())
day = input()

one = "Monday"
two = "Tuesday"
three = "Wednesday"
four = "Thursday"
five = "Friday"
six = "Saturday"

if 10 <= hour < 18 and (day == one or day == two or day == three or day == four or day == five or day == six):
    print("open")
else:
    print("closed")