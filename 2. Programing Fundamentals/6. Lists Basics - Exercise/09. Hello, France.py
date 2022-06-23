collection_of_items = input().split("|")
budget = float(input())
bought_items = []
profit = 0
revenue = 0

for i in collection_of_items:
    item_values = i.split("->")
    type_of_item = item_values[0]
    price_of_item = float(item_values[1])
    within_price_range = False
    if budget < price_of_item:
        continue
    if type_of_item == "Clothes":
        if price_of_item <= 50.00:
            budget -= price_of_item
            within_price_range = True
    elif type_of_item == "Shoes":
        if price_of_item <= 35.00:
            budget -= price_of_item
            within_price_range = True
    elif type_of_item == "Accessories":
        if price_of_item <= 20.50:
            budget -= price_of_item
            within_price_range = True
    if within_price_range:
        sold_item = price_of_item * 1.40
        profit += sold_item - price_of_item
        revenue += sold_item
        bought_items.append(f"{sold_item:.2f}")

total_money = revenue + budget

for price in bought_items:
    print(price, end=" ")
print()
print(f"Profit: {profit:.2f}")

if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")