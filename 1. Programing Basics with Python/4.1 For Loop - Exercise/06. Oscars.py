name_of_actor = input()
total_points = float(input())
number_of_judges = int(input())
#is_niminated = False

for i in range(number_of_judges):
    current_name = input()
    current_points = float(input())
    current_final_points = len(current_name) * current_points / 2
    total_points += current_final_points
    if total_points > 1250.5:
        #is_nominated = True
        break

if total_points > 1250.5: # if is_nominated = True
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")