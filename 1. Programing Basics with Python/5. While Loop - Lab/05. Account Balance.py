current_payment = input()
sum_money = 0

while current_payment != "NoMoreMoney":
    current_payment = float(current_payment)
    if current_payment < 0:
        print("Invalid operation!")
        break
    sum_money += current_payment
    print(f"Increase: {current_payment:.2f}")
    current_payment = input()

print(f"Total: {sum_money:.2f}")
    