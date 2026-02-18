budget = float(input())
season = input()

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent = budget * 0.3
    elif season == "winter":
        money_spent = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = budget * 0.4
    elif season == "winter":
        money_spent = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    money_spent = budget * 0.9

if season == "winter" or destination == "Europe":
    holiday_type = "Hotel"
else:
    holiday_type = "Camp"

print(f"Somewhere in {destination}")
print(f"{holiday_type} - {money_spent:.2f}")