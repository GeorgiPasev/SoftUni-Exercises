def total_price(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    if product == "coke":
        price = 1.40
    if product == "water":
        price = 1.00
    if product == "snacks":
        price = 2.00
    return f'{price * quantity:.2f}'


type_of_product = input()
amount = int(input())

print(total_price(type_of_product, amount))