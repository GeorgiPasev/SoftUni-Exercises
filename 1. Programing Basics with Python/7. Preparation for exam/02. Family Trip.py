budget = float(input())
count_nights = int(input())
price_per_night = float(input())
percent_extra_costs = int(input())

budget -= budget * percent_extra_costs / 100
if count_nights > 7:
    price_per_night *= 0.95
total_price = count_nights * price_per_night

diff = abs(budget - total_price)
if budget >= total_price:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")