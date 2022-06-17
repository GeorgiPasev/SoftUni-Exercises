budget = int(input())
season = input()
number_of_fishermen = int(input())

if season == "Spring":
    rent_of_ship = 3000
elif season == "Summer" or season == "Autumn":
    rent_of_ship = 4200
elif season == "Winter":
    rent_of_ship = 2600

if number_of_fishermen <= 6:
    rent_of_ship *= 0.9 # 10% discount
elif 7 <= number_of_fishermen <= 11:
    rent_of_ship *= 0.85 # 15% discount
elif number_of_fishermen >= 12:
    rent_of_ship *= 0.75 # 25% discount

if number_of_fishermen % 2 == 0 and not season == "Autumn": # even
    rent_of_ship *= 0.95

difference = abs(budget - rent_of_ship)

if budget >= rent_of_ship:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")