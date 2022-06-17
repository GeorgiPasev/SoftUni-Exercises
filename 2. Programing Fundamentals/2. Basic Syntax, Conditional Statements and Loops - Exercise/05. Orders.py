number_of_orders = int(input())
total_price = 0

for i in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_needed_day = int(input())
    if not 0.01 <= capsule_price <= 100:
        continue
    elif not 1 <= days <= 31:
        continue
    elif not 1 <= capsules_needed_day <= 2000:
        continue
    current_coffee_price = capsule_price * capsules_needed_day * days
    print(f"The price for the coffee is: ${current_coffee_price:.2f}")
    total_price += current_coffee_price

print(f"Total: ${total_price:.2f}")
