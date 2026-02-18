budget = float(input())
video_cards = int(input())
processors = int(input())
ram_cards = int(input())

video_card_price = video_cards * 250
processor_price = 0.35 * video_card_price * processors
ram_card_price = 0.1 * video_card_price * ram_cards
price = video_card_price + processor_price + ram_card_price

if video_cards > processors:
    price *= 0.85

if budget >= price:
    money_left = budget - price
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")