strawberries_price_kg = float(input())
bananas_in_kg = float(input())
oranges_in_kg = float(input())
raspberries_in_kg = float(input())
strawberries_in_kg = float(input())

raspberries_price_kg = strawberries_price_kg / 2
oranges_price_kg = raspberries_price_kg * 0.6
bananas_price_kg = raspberries_price_kg * 0.2

strawberries_price_needed = strawberries_in_kg * strawberries_price_kg
bananas_price_needed = bananas_in_kg * bananas_price_kg
oranges_price_needed = oranges_in_kg * oranges_price_kg
raspberries_price_needed = raspberries_in_kg * raspberries_price_kg

total = strawberries_price_needed + bananas_price_needed +\
    oranges_price_needed + raspberries_price_needed
print(f"{total:.2f}")
