budget = float(input())
price_per_kg_flour = float(input())

price_pack_eggs = price_per_kg_flour * 0.75
price_1liter_milk = price_per_kg_flour * 1.25

price_recipe_bread = price_pack_eggs + price_per_kg_flour + \
    price_1liter_milk / 4

coloured_eggs_collected = 0
bread_counter = 0

while budget >= price_recipe_bread:
    coloured_eggs_collected += 3
    bread_counter += 1
    if bread_counter % 3 == 0:
        coloured_eggs_collected -= bread_counter - 2
    budget -= price_recipe_bread

print(f"You made {bread_counter} loaves of Easter bread! Now you have {coloured_eggs_collected} eggs and {budget:.2f}BGN left.")