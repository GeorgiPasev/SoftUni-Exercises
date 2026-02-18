# input real number kv. metri]
# print "The final price is: {крайна цена на услугата} lv."
# "The discount is: {отстъпка} lv."

square_meters = float(input())
normal_price = 7.61 * square_meters
discount = 18/100 * normal_price
price_with_discount = normal_price - discount
print(f"The final price is: {price_with_discount} lv.")
print(f"The discount is: {discount} lv.")
