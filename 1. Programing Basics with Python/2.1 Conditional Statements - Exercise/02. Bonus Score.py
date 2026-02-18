number = int(input())
bonus_points = 0 

if number <= 100:
    bonus_points += 5
elif 1000 >= number > 100:
    bonus_points += number * 0.2
elif number > 1000:
    bonus_points += number * 0.1

if number % 2 == 0:
    bonus_points += 1

if number % 2 == 1 and number % 5 == 0: # check for odd and check for remainder of 0
    bonus_points += 2

print(bonus_points)
print(number + bonus_points)
