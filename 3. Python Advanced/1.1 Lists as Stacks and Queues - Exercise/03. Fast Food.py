from collections import deque

total_food = int(input())
orders = deque(map(int, input().split()))
orders_complete = True

print(max(orders))

for i in range(len(orders)):
    if total_food >= orders[0]:
        total_food -= orders.popleft()
    else:
        orders_complete = False
        break

if orders_complete:
    print("Orders complete")
else:
    #print(f"Orders left: " + " ".join(map(str, orders)))
    print(f"Orders left:", *orders, sep=" ")


# while orders[0] <= total_food:
#     total_food -= orders.popleft()

#     if not orders:
#         orders_complete = True #invert the other True
#         break