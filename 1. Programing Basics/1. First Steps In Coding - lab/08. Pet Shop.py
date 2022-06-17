# input number of boxes of food for dogs
# input same for cats
# print "{крайната сума} lv."

number_of_boxes_dogfood = int(input())
number_of_boxes_catfood = int(input())
money_needed = number_of_boxes_dogfood * 2.5 + number_of_boxes_catfood * 4
print(f"{money_needed} lv.")