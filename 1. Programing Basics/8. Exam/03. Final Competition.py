number_of_dancers = int(input())
points = float(input())
season = input()
place = input()

if place == "Bulgaria":
    points *= number_of_dancers
    if season == "summer":
        points *= 0.95
    elif season == "winter":
        points *= 0.92
elif place == "Abroad":
    points += (points * number_of_dancers) * 0.5
    if season == "summer":
        points *= 0.9
    elif season == "winter":
        points *= 0.85

charity_sum = points * 0.75
money_per_dancer = (points - charity_sum) / number_of_dancers


print(f"Charity - {charity_sum:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
    