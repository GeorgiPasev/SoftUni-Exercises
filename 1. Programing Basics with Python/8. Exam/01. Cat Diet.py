percent_fat = int(input())
percent_protein = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_water = int(input())

total_fat_gr = (percent_fat / 100 * total_calories) / 9
total_protein_gr = (percent_protein / 100 * total_calories) / 4
total_carbohydrates_gr = (percent_carbohydrates / 100 * total_calories) / 4

food_weight = total_fat_gr + total_protein_gr + total_carbohydrates_gr
calories_per_gr_food = total_calories / food_weight

result_calories = (100 - percent_water) / 100 * calories_per_gr_food

print(f"{result_calories:.4f}")
