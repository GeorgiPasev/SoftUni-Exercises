holiday_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
tedy_bears = int(input())
minions = int(input())
trucks = int(input())

price = puzzles * 2.6 + talking_dolls * 3 + tedy_bears * 4.1 + \
    minions * 8.2 + trucks * 2
number_of_toys = puzzles + talking_dolls + tedy_bears + minions + trucks

if number_of_toys >= 50:
    price *= 0.75

money_after_rent = price * 0.9
if money_after_rent >= holiday_price:
    money_left = money_after_rent - holiday_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = holiday_price - money_after_rent
    print(f"Not enough money! {money_needed:.2f} lv needed.")