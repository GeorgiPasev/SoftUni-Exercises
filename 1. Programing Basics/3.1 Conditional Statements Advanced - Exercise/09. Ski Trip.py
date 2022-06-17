days_staying = int(input())
room_type = input()
grade = input()

nights_number = days_staying - 1

if room_type == "room for one person":
    price = 18
elif room_type == "apartment":
    price = 25
    if days_staying < 10:
        price -= price * 0.3
    elif 10 <= days_staying <= 15:
        price -= price * 0.35
    else:
        price -= price * 0.5
elif room_type == "president apartment":
    price = 35
    if days_staying < 10:
        price -= price * 0.1
    elif 10 <= days_staying <= 15:
        price -= price * 0.15
    else:
        price -= price * 0.2

base_price = price * nights_number

if grade == "positive":
    base_price += base_price * 0.25
if grade == "negative":
    base_price -= base_price * 0.1

print(f"{base_price:.2f}")
