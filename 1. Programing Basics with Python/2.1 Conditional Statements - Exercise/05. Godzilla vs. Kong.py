budget = float(input())
number_of_statists = int(input())
price_clothing_one_statist = float(input())

decor = budget * 0.1
clothes = number_of_statists * price_clothing_one_statist
if number_of_statists > 150:
    clothes -= clothes * 0.1

if decor + clothes > budget:
    needed_money = (decor + clothes - budget)
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
else:
    enough_money = budget - (decor + clothes)
    print("Action!")
    print(f"Wingard starts filming with {enough_money:.2f} leva left.")
