money_needed_for_trip = float(input())
current_money = float(input())
consecutive_days_spending_counter = 0
days_passed = 0
# could also be done with bool variable

while consecutive_days_spending_counter < 5:
    days_passed += 1
    text_input = input()
    money_spent_or_saved = float(input())

    if text_input == "save":
        current_money += money_spent_or_saved
        consecutive_days_spending_counter = 0
        if money_needed_for_trip <= current_money:
            break
        continue
    if text_input == "spend":
        current_money -= money_spent_or_saved
        if current_money < 0:
            current_money = 0
    consecutive_days_spending_counter += 1


if consecutive_days_spending_counter == 5:
    print("You can't save the money.")
    print(f"{days_passed}")
else:
    print(f"You saved the money for {days_passed} days.")