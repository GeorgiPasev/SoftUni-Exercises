age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

cash = 0
sum = 0
toy_number = 0

for birthday in range(2, age + 1, 2):
    cash += 10
    sum += cash - 1

for birthday in range(1, age + 1, 2):
    toy_number += 1

final_sum = toy_number * toy_price + sum
difference = abs(final_sum - washing_machine_price)

if final_sum >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
