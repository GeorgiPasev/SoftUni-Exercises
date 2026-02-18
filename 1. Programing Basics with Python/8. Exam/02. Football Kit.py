shirt_price = float(input())
money_needed_for_ball = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.2
sport_shoes_price = (shirt_price + shorts_price) * 2
base_price = shirt_price + shorts_price + socks_price + sport_shoes_price
discounted_price = base_price * 0.85

diff = abs(discounted_price - money_needed_for_ball)
if discounted_price >= money_needed_for_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {discounted_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")