type_of_flower = input()
flowers_number = int(input())
budget = int(input())

price_per_flower = 0

if type_of_flower == "Roses":
    price_per_flower = 5
    if flowers_number > 80:
        price_per_flower *= 0.9 # 10% discount
elif type_of_flower == "Dahlias":
    price_per_flower = 3.8
    if flowers_number > 90:
        price_per_flower *= 0.85 # 15% discount
elif type_of_flower == "Tulips":
    price_per_flower = 2.8
    if flowers_number > 80:
        price_per_flower *= 0.85 # 15% discount
elif type_of_flower == "Narcissus":
    price_per_flower = 3
    if flowers_number < 120:
        price_per_flower *= 1.15 # 15% mark up
elif type_of_flower == "Gladiolus":
    price_per_flower = 2.5
    if flowers_number < 80:
        price_per_flower *= 1.2 # 20% mark up

needed_money = flowers_number * price_per_flower
difference = abs(budget - needed_money)

if budget >= needed_money:
    print(f"Hey, you have a great garden with {flowers_number} {type_of_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")