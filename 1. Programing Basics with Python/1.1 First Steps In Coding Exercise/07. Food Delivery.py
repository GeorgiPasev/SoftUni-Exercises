chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

main_course = chicken_menus * 10.35 + fish_menus * 12.4 + vegetarian_menus * 8.15
dessert = main_course * 0.2
price = main_course + dessert + 2.50
print(price)