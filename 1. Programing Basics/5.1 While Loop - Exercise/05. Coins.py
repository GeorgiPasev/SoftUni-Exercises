balance = float(input())
coin_counter = 0
# using round because we are using floating point numbers(fractions)
# another way to fix the problem is to convert the bgn into coins
# 0.5 BGN x 100 = 50 coins

while balance != 0:
    if balance >= 2:
        balance = round(balance - 2, 2)
        coin_counter += 1
        continue
    if balance >= 1:
        balance = round(balance - 1, 2)
        coin_counter += 1
        continue
    if balance >= 0.5:
        balance = round(balance - 0.5, 2)
        coin_counter += 1
        continue
    if balance >= 0.2:
        balance = round(balance - 0.2, 2)
        coin_counter += 1
        continue
    if balance >= 0.1:
        balance = round(balance - 0.1, 2)
        coin_counter += 1
        continue
    if balance >= 0.05:
        balance = round(balance - 0.05, 2)
        coin_counter += 1
        continue
    if balance >= 0.02:
        balance = round(balance - 0.02, 2)
        coin_counter += 1
        continue
    if balance >= 0.01:
        balance = round(balance - 0.01, 2)
        coin_counter += 1
        continue

print(coin_counter)

# alternative way to solve

# balance = float(input())
# balance = int(balance * 100)
# coin_counter = 0

# coin_counter += balance // 200 # number of times to increase counter
# balance %= 200 # storing remainder of coins into balance

# coin_counter += balance // 100
# balance %= 100

#etc

# print(coin_counter)