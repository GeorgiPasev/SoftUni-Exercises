number_of_snowballs = int(input())
highest_value_snowball = 0
highest_value_snowball_weight = 0
highest_value_snowball_time = 0
highest_value_snowball_quality = 0

for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value_of_snowball = (snowball_weight / snowball_time) ** snowball_quality
    if value_of_snowball > highest_value_snowball:
        highest_value_snowball = value_of_snowball
        highest_value_snowball_weight = snowball_weight
        highest_value_snowball_time = snowball_time
        highest_value_snowball_quality = snowball_quality

print(f"{highest_value_snowball_weight} : {highest_value_snowball_time} = {int(highest_value_snowball)} ({highest_value_snowball_quality})")
