group_number = int(input())

people_in_Musala = 0
people_in_Monblan = 0
people_in_Kilimandjaro = 0
people_in_K2 = 0
people_in_Everest = 0
all_people = 0
for group in range(group_number):
    current_people_in_group = int(input())
    all_people += current_people_in_group
    if current_people_in_group <= 5:
        people_in_Musala += current_people_in_group
    elif current_people_in_group <= 12:
        people_in_Monblan += current_people_in_group
    elif current_people_in_group <= 25:
        people_in_Kilimandjaro += current_people_in_group
    elif current_people_in_group <= 40:
        people_in_K2 += current_people_in_group
    else:
        people_in_Everest += current_people_in_group

percent_Musala = people_in_Musala / all_people * 100
percent_Monblan = people_in_Monblan / all_people * 100
percent_Kilimandjaro = people_in_Kilimandjaro / all_people * 100
percent_K2 = people_in_K2 / all_people * 100
percent_Everest = people_in_Everest / all_people * 100

print(f"{percent_Musala:.2f}%")
print(f"{percent_Monblan:.2f}%")
print(f"{percent_Kilimandjaro:.2f}%")
print(f"{percent_K2:.2f}%")
print(f"{percent_Everest:.2f}%")