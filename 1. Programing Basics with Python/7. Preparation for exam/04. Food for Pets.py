days = int(input())
total_food = float(input())
bisquit_reward = 0
food_eaten_by_dog = 0
food_eaten_by_cat = 0

for day in range(1, days + 1):
    food_eaten_by_dog_per_day = int(input())
    food_eaten_by_cat_per_day = int(input())
    food_eaten_by_dog += food_eaten_by_dog_per_day
    food_eaten_by_cat += food_eaten_by_cat_per_day
    if day % 3 == 0:
        bisquit_reward += (food_eaten_by_cat_per_day + food_eaten_by_dog_per_day) * 0.1

food_eaten = food_eaten_by_cat + food_eaten_by_dog
percent_food_eaten = food_eaten / total_food * 100
percent_eaten_by_cat = food_eaten_by_cat / food_eaten * 100
percent_eaten_by_dog = food_eaten_by_dog / food_eaten * 100

print(f"Total eaten biscuits: {round(bisquit_reward)}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_eaten_by_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_by_cat:.2f}% eaten from the cat.")