month = input()
number_of_nights_spend = int(input())

discount_apartment = 0
discount_studio = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < number_of_nights_spend <= 14:
        discount_studio = 0.05
    elif number_of_nights_spend > 14:
        discount_studio = 0.3
elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
    if number_of_nights_spend > 14:
        discount_studio = 0.2
elif month == "July" or month == "August":
    studio = 76
    apartment = 77

if number_of_nights_spend > 14:
    discount_apartment = 0.1

apartment -= apartment * discount_apartment
final_price_apartment = number_of_nights_spend * apartment
print(f"Apartment: {final_price_apartment:.2f} lv.")

studio -= studio * discount_studio
final_price_studio = number_of_nights_spend * studio
print(f"Studio: {final_price_studio:.2f} lv.")
